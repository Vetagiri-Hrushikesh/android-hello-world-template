# Android Hello World CookieCutter Template

A modern Android project template using Jetpack Compose, Kotlin, and the latest Android SDK. This template generates a complete Android project with customizable package names, app names, and configuration.

## Features

- 🚀 **Jetpack Compose** - Modern UI toolkit
- 📱 **Android SDK 35** - Latest Android APIs
- 🎨 **Material 3** - Modern design system
- 🧪 **Testing Setup** - Unit and instrumented tests
- ⚡ **Kotlin** - Modern Android development
- 🔧 **Fully Customizable** - Package names, app names, SDK versions

## Prerequisites

- **CookieCutter**: Install cookiecutter if you haven't already
  ```bash
  pip install cookiecutter
  ```
- **Android Studio**: Latest version with Android SDK 35
- **Java 11+**: Required for Android development

## Quick Start

### 1. Generate a New Android Project

```bash
cookiecutter https://github.com/Vetagiri-Hrushikesh/android-hello-world-template.git
```

### 2. Follow the Interactive Prompts

The template will ask you for the following information:

| Prompt | Description | Default |
|--------|-------------|---------|
| `app_name` | Name of your Android app | HelloWorldApp |
| `package_name` | Java package name (e.g., com.company.app) | com.example.helloworldapp |
| `project_name` | Project directory name | HelloWorldApp |
| `min_sdk` | Minimum Android SDK version | 24 |
| `target_sdk` | Target Android SDK version | 35 |
| `compile_sdk` | Compile SDK version | 35 |
| `version_code` | App version code | 1 |
| `version_name` | App version name | 1.0.0 |
| `description` | App description | A simple Hello World Android app |
| `author_name` | Your name or company | AppInv |
| `author_email` | Your email | support@appinv.com |
| `website` | Your website | https://appinv.com |

### 3. Example Usage

```bash
$ cookiecutter https://github.com/Vetagiri-Hrushikesh/android-hello-world-template.git
  [1/12] app_name (HelloWorldApp): MyAwesomeApp
  [2/12] package_name (com.example.helloworldapp): com.mycompany.myawesomeapp
  [3/12] project_name (HelloWorldApp): MyAwesomeApp
  [4/12] min_sdk (24): 
  [5/12] target_sdk (35): 
  [6/12] compile_sdk (35): 
  [7/12] version_code (1): 
  [8/12] version_name (1.0.0): 
  [9/12] description (A simple Hello World Android app): My awesome Android app
  [10/12] author_name (AppInv): My Company
  [11/12] author_email (support@appinv.com): dev@mycompany.com
  [12/12] website (https://appinv.com): https://mycompany.com
```

## Testing Your Generated Project

### 1. Open in Android Studio

1. Launch Android Studio
2. Click "Open an existing Android Studio project"
3. Navigate to your generated project folder and select it
4. Wait for the project to sync and build

### 2. Build the Project

```bash
cd MyAwesomeApp
./gradlew build
```

### 3. Run on Device/Emulator

1. **Connect a device** or **start an emulator**
2. In Android Studio, click the green "Run" button (▶️)
3. Select your target device
4. The app will install and launch automatically

### 4. Verify the App

- The app should display "Hello Android!" on the screen
- Check that the app name in the launcher matches your `app_name`
- Verify the package name in Android Studio matches your `package_name`

### 5. Run Tests

```bash
# Run unit tests
./gradlew test

# Run instrumented tests (requires device/emulator)
./gradlew connectedAndroidTest
```

## Project Structure

The generated project includes:

- **Main Activity**: Jetpack Compose UI with "Hello Android!" message
- **Theme**: Material 3 theme with light/dark support
- **Tests**: Unit and instrumented test examples
- **Gradle Configuration**: Latest Android Gradle Plugin setup
- **Resource Files**: Properly configured strings, themes, and manifest

## Customization

### Adding Dependencies

Edit `app/build.gradle.kts` to add your dependencies:

```kotlin
dependencies {
    // Your dependencies here
    implementation("androidx.core:core-ktx:1.12.0")
    implementation("androidx.lifecycle:lifecycle-runtime-ktx:2.7.0")
    // ... more dependencies
}
```

### Modifying the UI

Edit `MainActivity.kt` to customize the UI:

```kotlin
@Composable
fun Greeting(name: String, modifier: Modifier = Modifier) {
    Text(
        text = "Hello $name!", // Customize this message
        modifier = modifier
    )
}
```

### Updating Theme

Edit `ui/theme/Theme.kt` to customize colors and styling.

## Troubleshooting

### Build Errors

1. **SDK Version Issues**: Ensure you have Android SDK 35 installed
2. **Gradle Sync**: Try "File > Sync Project with Gradle Files"
3. **Clean Build**: Run `./gradlew clean` then rebuild

### App Not Installing

1. **Enable Developer Options** on your device
2. **Enable USB Debugging** if using a physical device
3. **Check device compatibility** with your `min_sdk` setting

### Template Issues

1. **Update CookieCutter**: `pip install --upgrade cookiecutter`
2. **Clear Cache**: Delete `~/.cookiecutters/` folder
3. **Re-download**: Use the full GitHub URL to re-download

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This template is open source and available under the MIT License.

## Support

If you encounter any issues:

1. Check the troubleshooting section above
2. Search existing GitHub issues
3. Create a new issue with detailed information

---

**Happy Android Development! 🚀** 