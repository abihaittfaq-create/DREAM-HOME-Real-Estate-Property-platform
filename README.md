# Lead Scoring & Intent Recognition System

## Overview

This project implements a Lead Scoring and Intent Recognition module for a real estate platform.

The purpose of this system is to analyze customer inquiries and identify customer intent along with lead priority. It helps in understanding customer requirements and identifying potential leads.

## Features

### 1. Intent Recognition

The system identifies the purpose of a customer's inquiry based on keywords.

Supported intents:

* Buy Property
* Rent Property
* Schedule Visit
* Price Inquiry
* General Inquiry

### 2. Lead Scoring

The system assigns a lead category based on customer interest and information provided in the inquiry.

Lead categories:

* High Lead
* Medium Lead
* Low Lead

The scoring is based on:

* Presence of budget or numerical information
* Mentioned location preferences
* Buying or visiting interest
* Urgency keywords

## Technologies Used

* Python
* JSON Data Processing
* Regular Expressions (Regex)
* Google Colab

## Project Files

```
Lead-Scoring-Intent-Recognition/

│── README.md
│── lead scoring.py
│── inquiries.json
```

## Working Process

1. User uploads the inquiry dataset (`inquiries.json`).
2. The system processes all existing customer inquiries from the dataset.
3. Intent Recognition identifies the customer's requirement.
4. Lead Scoring calculates the priority level of each inquiry.
5. The user can also enter a new custom inquiry manually.
6. The system predicts the intent and lead score for the new user query.


## Example

Input:

```
I want to buy a house in DHA Lahore urgently with a budget of 2 crore.
```

Output:

```
Intent: Buy Property

Lead Score: High
```


```

