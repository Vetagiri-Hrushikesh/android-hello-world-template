package {{ cookiecutter.package_name }}.ui.theme

import androidx.compose.material3.Typography
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.sp

// Set of Material typography styles to start with
val Typography = Typography(
    bodyLarge = TextStyle(
        fontFamily = FontFamily.Default,
        fontWeight = FontWeight.Normal,
        fontSize = {{ cookiecutter.typography_font_size }}.sp,
        lineHeight = {{ cookiecutter.typography_line_height }}.sp,
        letterSpacing = {{ cookiecutter.typography_letter_spacing }}.sp
    )
    /* Other default text styles to override
    titleLarge = TextStyle(
        fontFamily = FontFamily.Default,
        fontWeight = FontWeight.Normal,
        fontSize = {{ cookiecutter.title_large_font_size }}.sp,
        lineHeight = {{ cookiecutter.title_large_line_height }}.sp,
        letterSpacing = {{ cookiecutter.title_large_letter_spacing }}.sp
    ),
    labelSmall = TextStyle(
        fontFamily = FontFamily.Default,
        fontWeight = FontWeight.Medium,
        fontSize = {{ cookiecutter.label_small_font_size }}.sp,
        lineHeight = {{ cookiecutter.label_small_line_height }}.sp,
        letterSpacing = {{ cookiecutter.typography_letter_spacing }}.sp
    )
    */
) 