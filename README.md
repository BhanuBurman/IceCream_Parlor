# Ice Cream Parlor Application

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Setup and Running the Application](#setup-and-running-the-application)
  - [Step 1: Clone the repository](#step-1-clone-the-repository)
  - [Step 2: Run the application](#step-2-run-the-application)
- [Docker Instructions](#docker-instructions)
  - [Step 1: Build the Docker image](#step-1-build-the-docker-image)
  - [Step 2: Run the Docker container](#step-2-run-the-docker-container)
- [Documentation of Test Steps](#documentation-of-test-steps)
  - [Add Seasonal Flavor](#add-seasonal-flavor)
  - [Add Ingredient](#add-ingredient)
  - [Add Flavor Suggestion](#add-flavor-suggestion)
  - [Add Allergen](#add-allergen)
  - [Add to Cart](#add-to-cart)
  - [Search Flavors](#search-flavors)
  - [Remove from Cart](#remove-from-cart)
- [SQL Queries](#sql-queries)
  - [Create Tables](#create-tables)
  - [Insert a Seasonal Flavor](#insert-a-seasonal-flavor)
  - [Select All Seasonal Flavors](#select-all-seasonal-flavors)

## Overview
This is a simple command-line application to manage an ice cream parlor. It uses SQLite for managing data such as seasonal flavor offerings, ingredient inventory, customer flavor suggestions, and allergy concerns.

## Features
- Maintain a cart of favorite products.
- Search & filter offerings.
- Add allergens if they don't already exist.
- CRUD operations for seasonal flavors, ingredients, suggestions, and allergens.

## Requirements
- Python 3.12.2
- SQLite (Included in Python standard library)

## Setup and Running the Application

### Step 1: Clone the repository

```sh
git clone https://github.com/your-repo/ice_cream_parlor.git
cd ice_cream_parlor
```

### Step 2: Run the appllication

```sh
python ice_cream_parlor.py
```
## Docker Instructions

### Step 1: Build the Docker image

```sh
docker build -t ice_cream_parlor .
```
### Step 2: Run the Docker container

```sh
docker run -it --rm ice_cream_parlor
```

## Documentation of test steps

### Add Seasonal Flavor:
Navigate to Add Seasonal Flavor in the menu and input the flavor details.
Verify that the flavor is added by selecting View Seasonal Flavors.
```sh
Enter your choice: 1
Enter flavor name: Mango Delight
Enter flavor description: A tropical mango-flavored ice cream.
```

### Add Ingredient:
Navigate to Add Ingredient in the menu and input the ingredient details.
Verify that the ingredient is added by selecting View Ingredients.
```sh
Enter your choice: 3
Enter ingredient name: Mango
Enter quantity: 50
```

### Add Flavor Suggestion:
Navigate to Add Flavor Suggestion in the menu and input the flavor suggestion details.
Verify that the suggestion is added by selecting View Flavor Suggestions.
```sh
Enter your choice: 5
Enter flavor name: Coconut Bliss
Enter allergy concerns: None
```

### Add Allergen:
Navigate to Add Allergen in the menu and input the allergen details.
Verify that the allergen is added by selecting View Allergens.
```sh
Enter your choice: 7
Enter allergen name: Nuts
```

### Add to Cart:
Navigate to Add to Cart in the menu and input the product details.
Verify that the product is added to the cart by selecting View Cart.
```sh
Enter your choice: 9
Enter product ID: 1
Enter product name: Mango Delight
```

### Search Flavors:
Navigate to Search Flavors in the menu and input the search keyword.
Verify that the search results are displayed.
```sh
Enter your choice: 12
Enter search keyword: Mango
```

### Remove from Cart:
Navigate to Remove from Cart in the menu and input the product ID.
Verify that the product is removed from the cart by selecting View Cart.
```sh
Enter your choice: 11
Enter product ID to remove: 1
```

## SQL Queries
Here are some SQL queries used in the application:
### create tables
```sh
CREATE TABLE IF NOT EXISTS seasonal_flavors (
    id INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT
);
CREATE TABLE IF NOT EXISTS ingredients (
    id INTEGER PRIMARY KEY,
    name TEXT,
    quantity INTEGER
);
CREATE TABLE IF NOT EXISTS suggestions (
    id INTEGER PRIMARY KEY,
    flavor_name TEXT,
    allergy_concerns TEXT
);
CREATE TABLE IF NOT EXISTS allergens (
    id INTEGER PRIMARY KEY,
    name TEXT
);
CREATE TABLE IF NOT EXISTS cart (
    id INTEGER PRIMARY KEY,
    product_id INTEGER,
    product_name TEXT
);
```

### Insert a seasonal flavour
```sh
INSERT INTO seasonal_flavors (name, description) VALUES (?, ?);
```

### Select all seasonal flavors:
```sh
SELECT * FROM seasonal_flavors;
```









