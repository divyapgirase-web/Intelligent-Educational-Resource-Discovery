import pandas as pd
import matplotlib.pyplot as plt


def get_category_counts(dataframe):
    """
    Return the number of resources in each category.
    """

    return dataframe["category"].value_counts()


def create_category_chart(dataframe):
    """
    Create a bar chart showing resources by category.
    """

    counts = get_category_counts(dataframe)

    figure = plt.figure(figsize=(9, 5))

    counts.plot(kind="bar")

    plt.title("Educational Resources by Category")
    plt.xlabel("Category")
    plt.ylabel("Number of Resources")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    return figure