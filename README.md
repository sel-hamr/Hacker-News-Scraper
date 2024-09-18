# Hacker News Scraper

## Description
This script scrapes articles from Hacker News and filters them based on the number of votes. The user can specify the number of articles to display and the minimum number of votes required.

## Functions

### `filter_data_hacker_new(links, votes, minimum_point)`
Filters the articles based on the minimum number of votes.

- **Parameters:**
  - `links` (list): List of article links.
  - `votes` (list): List of vote counts corresponding to the articles.
  - `minimum_point` (int): Minimum number of votes required for an article to be included in the result.

- **Returns:**
  - `list`: A list of dictionaries containing the title, link, and votes of the filtered articles.

### `main()`
Main function that drives the script. It prompts the user for input and scrapes Hacker News articles based on the provided criteria.

- **Prompts:**
  - `number_of_item` (int): Number of articles to display.
  - `point` (int): Minimum number of votes required for an article to be displayed.

- **Process:**
  - Scrapes Hacker News articles.
  - Filters the articles based on the minimum number of votes.
  - Displays the filtered articles.

## Usage
1. Run the script:
    ```sh
    python test.py
    ```
2. Enter the number of articles you want to see when prompted.
3. Enter the minimum number of votes you want to see when prompted.

## Example
```sh
python test.py
