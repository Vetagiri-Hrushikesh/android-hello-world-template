# Android Hello World Template

A professional, production-ready cookiecutter template for creating Android Hello World applications using modern Android development practices.

## 🚀 Features

- **Modern Android Development**: Kotlin + Jetpack Compose
- **Clean Architecture**: Well-structured project layout
- **Professional Setup**: Optimized build configuration
- **Smart Variables**: Only essential, used variables (24 total)
- **Auto-Configuration**: Automatic project setup and naming
- **Testing Ready**: Unit tests and UI tests included
- **Material Design 3**: Modern UI components

## 📋 Requirements

Run the version detection script to check your environment:

```bash
python scripts/version_detector.py > requirements.md
```

### Minimum Requirements
- **Java**: 11 or higher
- **Kotlin**: 1.9.0 or higher
- **Gradle**: 8.0 or higher
- **Android SDK**: API 35 (Android 15)
- **Android Studio**: Latest stable version

## 🛠️ Installation

### 1. Install Cookiecutter
```bash
pip install cookiecutter
```

### 2. Generate Project
```bash
# From GitHub
cookiecutter https://github.com/Vetagiri-Hrushikesh/android-hello-world-template.git

# Or from local directory
cookiecutter android-hello-world-template
```

### 3. Follow the Prompts
The template will ask for 24 essential configuration values:

| Category | Variables | Description |
|----------|-----------|-------------|
| **Project** | 4 | Name, package, description, author info |
| **Build** | 8 | SDK versions, Java version, Gradle config |
| **UI** | 12 | Typography, navigation, theme settings |

## 📁 Project Structure

```
{{cookiecutter.project_name}}/
├── app/
│   ├── src/
│   │   ├── main/
│   │   │   ├── java/{{cookiecutter.package_name}}/
│   │   │   │   ├── MainActivity.kt
│   │   │   │   └── ui/theme/
│   │   │   └── res/
│   │   ├── test/
│   │   └── androidTest/
│   └── build.gradle.kts
├── gradle/
├── build.gradle.kts
└── settings.gradle.kts
```

## 🎯 What You Get

### ✅ Ready-to-Run App
- **Hello World Screen**: Professional UI with Material Design 3
- **Version Display**: Shows app version and welcome message
- **Responsive Layout**: Works on all screen sizes
- **Dark/Light Theme**: Automatic theme support

### ✅ Development Setup
- **Gradle Wrapper**: No need to install Gradle globally
- **Dependencies**: All necessary Android libraries included
- **Build Configuration**: Optimized for development and release
- **Code Style**: Consistent Kotlin coding standards

### ✅ Testing Framework
- **Unit Tests**: JUnit 4 setup with example test
- **UI Tests**: Espresso setup with example test
- **Test Runner**: Configured for Android testing

## 🚀 Quick Start

1. **Generate the project** (see Installation above)
2. **Open in Android Studio**:
   ```bash
   cd {{cookiecutter.project_name}}
   # Open Android Studio and select "Open an existing project"
   ```
3. **Run the app**:
   - Select a device/emulator
   - Click the Run button (▶️) or press `Shift + F10`

## 🔧 Customization

### Typography
The template uses configurable typography variables:
- `typography_font_size`: Base font size (16sp)
- `title_large_font_size`: Title font size (22sp)
- `label_small_font_size`: Small text size (11sp)

### Navigation
- `navigation_style`: Choose between "edge_to_edge" or standard navigation

### Build Configuration
- `min_sdk`: Minimum Android API level (24)
- `target_sdk`: Target Android API level (35)
- `compile_sdk`: Compilation SDK version (35)

## 📱 App Features

### Main Screen
- **Globe Icon**: Material Design icon
- **Hello World Text**: Large, bold title
- **Welcome Message**: App name display
- **Version Info**: Shows current app version

### UI Components
- **Material Design 3**: Modern design system
- **Responsive Layout**: Adapts to different screen sizes
- **Theme Support**: Automatic dark/light mode
- **Accessibility**: Proper content descriptions

## 🧪 Testing

### Unit Tests
```bash
./gradlew test
```

### UI Tests
```bash
./gradlew connectedAndroidTest
```

### All Tests
```bash
./gradlew check
```

## 📦 Build & Deploy

### Debug Build
```bash
./gradlew assembleDebug
```

### Release Build
```bash
./gradlew assembleRelease
```

### APK Location
```
app/build/outputs/apk/debug/app-debug.apk
```

## 🔍 Troubleshooting

### Common Issues

1. **Gradle Sync Failed**
   - Check internet connection
   - Update Android Studio
   - Invalidate caches (File → Invalidate Caches)

2. **Build Errors**
   - Clean project (Build → Clean Project)
   - Rebuild project (Build → Rebuild Project)

3. **Emulator Issues**
   - Create new AVD in Android Studio
   - Enable hardware acceleration

### Performance Tips

- Use Android Studio's built-in profiler
- Enable R8 optimization for release builds
- Use vector drawables for better performance

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This template is provided as-is for educational and development purposes.

## 🙏 Acknowledgments

- **Jetpack Compose**: Modern Android UI toolkit
- **Material Design**: Google's design system
- **Cookiecutter**: Project template generator

---

**Made with ❤️ for the Android development community**

*Generated with Android Hello World Template v1.0.0* 