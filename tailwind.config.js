import defaultTheme from 'tailwindcss/defaultTheme'

module.exports = {
  prefix: 'tw-',
  plugins: [require('@tailwindcss/typography')],
  theme: {
    // Controls content theme
    colors: {
      gray: defaultTheme.colors.coolGray,
      blue: defaultTheme.colors.lightBlue,
      red: defaultTheme.colors.rose,
      pink: defaultTheme.colors.fuchsia,
    },
    fontFamily: {
      sans: ['Graphik', 'sans-serif'],
      serif: ['Merriweather', 'serif'],
    },
    extend: {
      spacing: {
        128: '32rem',
        144: '36rem',
      },
      borderRadius: {
        '4xl': '2rem',
      },
    },
  },
}
