
# Word of the Day - Static Website

This project is a **Word of the Day** static website that displays a random word, its meaning, and an example sentence from a predefined list stored in a CSV file. Users can click a button to view another random word. The site is built using HTML, CSS, and JavaScript, making it deployable on platforms like **GitHub Pages** and **Netlify**.

## Features

- **Random Word Generation**: Displays a random word from a CSV file when the page loads.
- **Dynamic Word Refresh**: Users can click the "Show Another Word" button to fetch and display a new random word.
- **Static Deployment**: No backend required. Can be deployed on static hosting platforms such as GitHub Pages or Netlify.
- **Responsive Design**: Works well on mobile and desktop devices.

## Project Structure

```
word_of_the_day/
│
├── index.html        # Main HTML file
├── static/
│   └── style.css     # CSS for styling
├── words_list.csv    # CSV file containing the list of words, meanings, and examples
└── script.js         # JavaScript for handling CSV parsing and interactivity
```

### Files Explained:

- `index.html`: The main structure of the webpage.
- `style.css`: Contains the CSS styles for a clean, modern look and responsiveness.
- `words_list.csv`: Stores the list of words, meanings, and example sentences.
- `script.js`: Contains JavaScript that loads the CSV file, picks random words, and dynamically updates the HTML content.

## How It Works

1. When the page loads, the `script.js` file reads the `words_list.csv` file, parses it, and selects a random word.
2. The word, its meaning, and example sentence are displayed on the page.
3. Users can click the **"Show Another Word"** button to view a new random word.

## CSV File Format

The `words_list.csv` file should follow this format:

```csv
Word,Meaning,Example
Articulate,Express clearly and effectively,"She was able to articulate her thoughts during the meeting."
Diligent,Showing care and effort,"He is very diligent in his work and always meets deadlines."
Resilient,Able to recover quickly from difficulties,"The resilient community rebuilt after the disaster."
...
```

## Development Setup

If you want to make changes or run the site locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/word_of_the_day.git
   ```

2. Open `index.html` in your browser directly, as the site does not require a local server to run (it’s fully static).

3. Edit the files as needed, then commit and push changes to your GitHub repository for automatic deployment.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```

3. Make your changes, commit, and push to your branch:
   ```bash
   git commit -m "Description of the changes"
   git push origin feature-name
   ```

4. Open a pull request, and describe the changes you've made.

##Contact
Gmail:chittithallikaja@gmail.com
