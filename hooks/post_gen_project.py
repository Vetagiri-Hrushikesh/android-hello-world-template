#!/usr/bin/env python3
"""
Post-generation hook for Android Hello World template.
This script validates inputs and sets up the generated project.
"""

import os
import sys
import json
from pathlib import Path

# Add scripts directory to path - fix the path resolution
template_dir = Path(__file__).parent.parent
scripts_dir = template_dir / "scripts"
sys.path.insert(0, str(scripts_dir))

try:
    from logger import logger
    from validator import validate_template_inputs
except ImportError:
    # Fallback if scripts are not available
    import logging
    
    # Create a simple logger
    logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')
    logger = logging.getLogger("AndroidTemplate")
    
    def validate_template_inputs(context):
        """Fallback validation function."""
        return True, [], []
    
    print("⚠️  Warning: Using fallback logging and validation")

def main():
    """Main function to handle post-generation tasks."""
    print("\n" + "="*50)
    print("🚀 Android Hello World Template Generation")
    print("="*50)
    
    # Get the project directory (current working directory after cookiecutter generation)
    project_dir = os.getcwd()
    project_name = os.path.basename(project_dir)
    
    print(f"Project directory: {project_dir}")
    print(f"Project name: {project_name}")
    
    # Load cookiecutter context
    context_file = Path(project_dir) / "cookiecutter_context.json"
    if context_file.exists():
        print("\n📌 Loading Template Context")
        with open(context_file, 'r') as f:
            context = json.load(f)
        
        print("✅ Template context loaded successfully")
        
        # Validate inputs
        print("\n📌 Validating Template Inputs")
        is_valid, errors, warnings = validate_template_inputs(context)
        
        if not is_valid:
            print("❌ Template validation failed!")
            print("Please fix the errors and regenerate the template.")
            sys.exit(1)
        
        if warnings:
            print("⚠️  Template generated with warnings. Please review:")
            for warning in warnings:
                print(f"  - {warning}")
        
        print("✅ Template validation completed successfully!")
        
    else:
        print("⚠️  Template context file not found, skipping validation")
        context = {}
    
    # Project setup steps
    print("\n📌 Project Setup")
    
    # Step 1: Verify project structure
    print("📋 Step 1/3: Verifying project structure")
    required_files = [
        "app/build.gradle.kts",
        "app/src/main/java",
        "app/src/main/AndroidManifest.xml",
        "build.gradle.kts",
        "settings.gradle.kts",
        "gradlew",
        "gradlew.bat"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(project_dir) / file_path:
            missing_files.append(file_path)
    
    if missing_files:
        print(f"❌ Missing required files: {missing_files}")
        sys.exit(1)
    
    print("✅ Project structure verified")
    
    # Step 2: Generate requirements file
    print("📋 Step 2/3: Generating requirements file")
    try:
        # Try to import and run version detector
        sys.path.insert(0, str(scripts_dir))
        from version_detector import generate_requirements_md
        requirements_content = generate_requirements_md()
        
        requirements_file = Path(project_dir) / "REQUIREMENTS.md"
        with open(requirements_file, 'w') as f:
            f.write(requirements_content)
        
        print("✅ Requirements file generated: REQUIREMENTS.md")
    except Exception as e:
        print(f"⚠️  Could not generate requirements file: {e}")
    
    # Step 3: Clean up temporary files
    print("📋 Step 3/3: Cleaning up temporary files")
    temp_file = Path(project_dir) / "cookiecutter_context.json"
    if temp_file.exists():
        temp_file.unlink()
        print("✅ Temporary files cleaned up")
    
    # Final success message
    print("\n" + "="*50)
    print("🚀 Generation Complete")
    print("="*50)
    print(f"✅ Android project '{project_name}' has been successfully generated!")
    
    # Display next steps
    print("\n📌 Next Steps")
    print("1. Open the project in Android Studio:")
    print(f"   cd {project_name}")
    print("   # Open Android Studio and select 'Open an existing project'")
    
    print("2. Sync the project with Gradle files")
    print("3. Build and run the project")
    print("4. Check REQUIREMENTS.md for environment details")
    
    # Display project info
    if context:
        print("\n📌 Project Information")
        print(f"📱 App Name: {context.get('app_name', 'Unknown')}")
        print(f"📦 Package: {context.get('package_name', 'Unknown')}")
        print(f"🔢 Version: {context.get('version_name', 'Unknown')}")
        print(f"👨‍💻 Author: {context.get('author_name', 'Unknown')}")
        print(f"📧 Email: {context.get('author_email', 'Unknown')}")
        print(f"🎯 Min SDK: {context.get('min_sdk', 'Unknown')}")
        print(f"🎯 Target SDK: {context.get('target_sdk', 'Unknown')}")
    
    print("\n🎉 Happy Android Development!")

if __name__ == "__main__":
    main() 