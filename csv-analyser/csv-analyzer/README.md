# Top 250 movie ratings analyser

This is my **first Python project** where I decided to explore working with CSV files and data analysis. I wanted to see what I could learn from the  top 250 movies dataset , like which movies are highest rated, which decades produced the best films, and how ratings relate to the number of votes. It looked like a good starter database to try basic python stuff on

Since I’m new to `pandas`, `numpy`, and `matplotlib`, this project was a great way to practice reading data, performing calculations, and visualizing results.

**Load and explore the dataset**

I started by reading the CSV using `pandas` to see what columns were available (`Title`, `Year`, `Rating`, `Rating Count`).

**Clean the data**

I realized that the `Rating Count` column had commas in the numbers (like `2,089,382`), so I needed to convert it to integers before doing any calculations.

**Compute statistics**

Using `numpy` and `pandas`, I calculated:

* Average, median, and standard deviation of ratings
* Highest and lowest rated movies
* Average number of votes
* Ratings grouped by decade

**Visualize the data**

I used `matplotlib` to create:

* A histogram of ratings
* A bar chart showing average ratings by decade
* A scatter plot of ratings vs number of votes
