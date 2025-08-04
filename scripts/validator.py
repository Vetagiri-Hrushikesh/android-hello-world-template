#!/usr/bin/env python3
"""
Validation system for Android Hello World template.
Validates user inputs and environment requirements.
"""

import re
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from .logger import logger

class AndroidTemplateValidator:
    """Validator for Android template inputs and environment."""
    
    def __init__(self):
        """Initialize the validator."""
        self.errors = []
        self.warnings = []
    
    def validate_project_name(self, name: str) -> bool:
        """Validate project name."""
        if not name:
            self.errors.append("Project name cannot be empty")
            return False
        
        if not re.match(r'^[A-Za-z][A-Za-z0-9_]*$', name):
            self.errors.append("Project name must start with a letter and contain only letters, numbers, and underscores")
            return False
        
        if len(name) > 50:
            self.errors.append("Project name must be 50 characters or less")
            return False
        
        # Check for reserved words
        reserved_words = ['android', 'test', 'main', 'java', 'kotlin', 'gradle']
        if name.lower() in reserved_words:
            self.warnings.append(f"Project name '{name}' might conflict with Android reserved words")
        
        return True
    
    def validate_package_name(self, package: str) -> bool:
        """Validate package name."""
        if not package:
            self.errors.append("Package name cannot be empty")
            return False
        
        # Android package name rules
        if not re.match(r'^[a-z][a-z0-9_]*(\.[a-z][a-z0-9_]*)*$', package):
            self.errors.append("Package name must follow Java package naming conventions (e.g., com.example.app)")
            return False
        
        if len(package) > 100:
            self.errors.append("Package name must be 100 characters or less")
            return False
        
        return True
    
    def validate_sdk_version(self, version: str, min_version: int = 21, max_version: int = 35) -> bool:
        """Validate SDK version."""
        try:
            version_int = int(version)
            if version_int < min_version or version_int > max_version:
                self.errors.append(f"SDK version must be between {min_version} and {max_version}")
                return False
        except ValueError:
            self.errors.append("SDK version must be a valid integer")
            return False
        
        return True
    
    def validate_java_version(self, version: str) -> bool:
        """Validate Java version."""
        try:
            version_int = int(version)
            if version_int < 8 or version_int > 21:
                self.errors.append("Java version must be between 8 and 21")
                return False
        except ValueError:
            self.errors.append("Java version must be a valid integer")
            return False
        
        return True
    
    def validate_email(self, email: str) -> bool:
        """Validate email address."""
        if not email:
            self.warnings.append("Email address is empty (optional but recommended)")
            return True
        
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            self.errors.append("Invalid email address format")
            return False
        
        return True
    
    def validate_version_name(self, version: str) -> bool:
        """Validate version name (semantic versioning)."""
        if not version:
            self.errors.append("Version name cannot be empty")
            return False
        
        # Semantic versioning pattern
        semver_pattern = r'^\d+\.\d+\.\d+(-[a-zA-Z0-9.-]+)?(\+[a-zA-Z0-9.-]+)?$'
        if not re.match(semver_pattern, version):
            self.warnings.append("Version name should follow semantic versioning (e.g., 1.0.0)")
        
        return True
    
    def validate_environment(self) -> bool:
        """Validate development environment."""
        logger.subsection("Environment Validation")
        
        # Check Java
        try:
            result = subprocess.run(['java', '-version'], capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                logger.success("Java is installed")
            else:
                self.errors.append("Java is not properly installed")
        except (subprocess.TimeoutExpired, FileNotFoundError):
            self.errors.append("Java is not installed")
        
        # Check Android SDK
        sdk_paths = [
            Path.home() / "Library/Android/sdk",
            Path.home() / "Android/Sdk",
            Path("C:/Users") / Path.home().name / "AppData/Local/Android/Sdk",
        ]
        
        sdk_found = False
        for sdk_path in sdk_paths:
            if sdk_path.exists():
                logger.success(f"Android SDK found at: {sdk_path}")
                sdk_found = True
                break
        
        if not sdk_found:
            self.warnings.append("Android SDK not found in common locations")
        
        # Check Android Studio
        studio_paths = [
            "/Applications/Android Studio.app",
            str(Path.home() / "android-studio"),
            "C:/Program Files/Android/Android Studio",
        ]
        
        studio_found = False
        for studio_path in studio_paths:
            if Path(studio_path).exists():
                logger.success("Android Studio is installed")
                studio_found = True
                break
        
        if not studio_found:
            self.warnings.append("Android Studio not found in common locations")
        
        return len(self.errors) == 0
    
    def validate_all(self, context: Dict[str, str]) -> Tuple[bool, List[str], List[str]]:
        """Validate all template inputs."""
        logger.section("Template Validation")
        
        # Validate required fields
        required_fields = {
            'project_name': self.validate_project_name,
            'package_name': self.validate_package_name,
            'min_sdk': lambda x: self.validate_sdk_version(x, 21, 35),
            'target_sdk': lambda x: self.validate_sdk_version(x, 21, 35),
            'compile_sdk': lambda x: self.validate_sdk_version(x, 21, 35),
            'java_version': self.validate_java_version,
            'version_name': self.validate_version_name,
        }
        
        for field, validator in required_fields.items():
            if field in context:
                if not validator(context[field]):
                    logger.error(f"Validation failed for {field}: {context[field]}")
            else:
                self.errors.append(f"Required field '{field}' is missing")
        
        # Validate optional fields
        if 'author_email' in context:
            self.validate_email(context['author_email'])
        
        # Validate environment
        self.validate_environment()
        
        # Log results
        if self.errors:
            logger.error(f"Found {len(self.errors)} validation errors")
            for error in self.errors:
                logger.error(f"  - {error}")
        
        if self.warnings:
            logger.warning(f"Found {len(self.warnings)} warnings")
            for warning in self.warnings:
                logger.warning(f"  - {warning}")
        
        if not self.errors and not self.warnings:
            logger.success("All validations passed successfully!")
        
        return len(self.errors) == 0, self.errors, self.warnings

def validate_template_inputs(context: Dict[str, str]) -> Tuple[bool, List[str], List[str]]:
    """Validate template inputs and return results."""
    validator = AndroidTemplateValidator()
    return validator.validate_all(context) 