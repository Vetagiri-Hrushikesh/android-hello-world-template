plugins {
    alias(libs.plugins.android.application)
    alias(libs.plugins.kotlin.android)
    alias(libs.plugins.kotlin.compose)
}

android {
    namespace = "{{ cookiecutter.package_name }}"
    compileSdk = {{ cookiecutter.compile_sdk }}

    defaultConfig {
        applicationId = "{{ cookiecutter.package_name }}"
        minSdk = {{ cookiecutter.min_sdk }}
        targetSdk = {{ cookiecutter.target_sdk }}
        versionCode = {{ cookiecutter.version_code }}
        versionName = "{{ cookiecutter.version_name }}"

        testInstrumentationRunner = "{{ cookiecutter.test_instrumentation_runner }}"
    }

    buildTypes {
        release {
            isMinifyEnabled = false
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_{{ cookiecutter.java_version }}
        targetCompatibility = JavaVersion.VERSION_{{ cookiecutter.java_version }}
    }
    kotlinOptions {
        jvmTarget = "{{ cookiecutter.java_version }}"
    }
    buildFeatures {
        compose = true
    }
}

dependencies {

    implementation(libs.androidx.core.ktx)
    implementation(libs.androidx.lifecycle.runtime.ktx)
    implementation(libs.androidx.activity.compose)
    implementation(platform(libs.androidx.compose.bom))
    implementation(libs.androidx.ui)
    implementation(libs.androidx.ui.graphics)
    implementation(libs.androidx.ui.tooling.preview)
    implementation(libs.androidx.material3)
    testImplementation(libs.junit)
    androidTestImplementation(libs.androidx.junit)
    androidTestImplementation(libs.androidx.espresso.core)
    androidTestImplementation(platform(libs.androidx.compose.bom))
    androidTestImplementation(libs.androidx.ui.test.junit4)
    debugImplementation(libs.androidx.ui.tooling)
    debugImplementation(libs.androidx.ui.test.manifest)
}