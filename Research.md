# Readability

## Table of Contents

  - [English Readability Tests](#english-readability-tests)
    - [Flesch-Kincaid Reading Ease](#flesch-kincaid-reading-ease)
    - [Automated Readability Index (ARI)](#automated-readability-index-ari)
    - [Coleman-Liau](#coleman-liau)
    - [Gunning Fog](#gunning-fog)
    - [LIX](#lix)
    - [SMOG (Simple Measure of Gobbledygook)](#smog-simple-measure-of-gobbledygook)
  - [Spanish Readability Tests](#spanish-readability-tests)
    - [Fernandez Huerta Index](#fernandez-huerta-index)
    - [The Szigriszt-Pazo Perspicuity Index](#the-szigriszt-pazo-perspicuity-index)
    - [Gutiérrez de Polini's Readability Formula](#gutiérrez-de-polinis-readability-formula)
  - [Online Readability Tools](#online-readability-tools)
    - [Grammarly](#grammarly)
    - [LLMs (ChatGPT, Gemini, & Copilot)](#llms-chatgpt-gemini--copilot)
    - [Hemingway Editor](#hemingway-editor)
    - [Rewordify](#rewordify)
  - [Overall Analysis](#overall-analysis)
    - [Similarities](#similarities)
    - [Standout Features](#standout-features)
  - [Proposed Readability Test](#proposed-readability-test)
    - [Areas to Address](#areas-to-address)
    - [Challenges](#challenges)
    - [Use Case](#use-case)

## English Readability Tests

### Flesch-Kincaid Reading Ease

#### Equation

$206.835 - 1.015(\frac{TW}{TS}) - 84.6(\frac{TW}{TSy})$

- *TW* = Total Words
- *TS* = Total Sentences
- *TSy* = Total Syllables

#### Readability Scorecard

| Score | School Level (Difficulty) |
|---|---|
| 90.0 - 100.0+ | 5th grade and lower |
| 80.0 - 90.0 | 6th grade |
| 70.0 - 80.0 | 7th grade |
| 60.0 - 70.0 | 8th & 9th grade |
| 50.0 - 60.0 | 10th - 12th grade |
| 30.0 - 50.0 | College |
| 0.0 - 30.0 | College Grad |

#### Overview

### Automated Readability Index (ARI)

#### Equation

$4.71(\frac{C}{W}) + 0.5(\frac{W}{S}) - 21.43$

- *C* = Characters (Number of letters and numbers)
- *W* = Words (Number of Spaces)
- *S* = Sentences

#### Readability Scorecard

| Score | Grade Level |
|---|---|
| &le; 1 | Kindergarten |
| 2 | 1st grade |
| 3 | 2nd grade |
| 4 | 3rd grade |
| 5 | 4th grade |
| 6 | 5th grade |
| 7 | 6th grade |
| 8 | 7th grade |
| 9 | 8th grade |
| 10 | 9th grade |
| 11 | 10th grade |
| 12 | 11th grade |
| 13 | 12th grade |
| 14 | College |


#### Overview

### Coleman-Liau

#### Equation
$CLI = 0.0588L - 0.296S -15.8$

- *L* = average number of letters per 100 words
- *S* = average number of sentences per 100 words
- *Content needs to be 100+ words*

#### Readability Scorecard

| Score (Approx.) | U.S. Grade Level         |
|------------------|--------------------------|
| 6.0–6.9           | 6th Grade                |
| 7.0–7.9           | 7th Grade                |
| 8.0–8.9           | 8th Grade                |
| 9.0–9.9           | 9th Grade (Freshman HS)  |
| 10.0–10.9         | 10th Grade               |
| 11.0–11.9         | 11th Grade               |
| 12.0–12.9         | 12th Grade (Senior HS)   |
| 13.0–13.9         | 1st Year College         |
| 14.0–14.9         | 2nd Year College         |


#### Overview

### Gunning Fog

#### Equation
$0.4[(\frac{W}{S}) + 100(\frac{CW}{W})]$

- *W* = Words
- *S* = Sentences
- *CW* = Complex Words
- *Content needs to be 100+ words*

#### Readability Scorecard

| Fog Index | Reading Level by Grade |
|---|---|
| &le; 6 | 6th grade |
| 7 | 7th grade |
| 8 | 8th grade |
| 9 | 9th grade |
| 10 | 10th grade |
| 11 | 11th grade |
| 12 | 12th grade |
| 13 | College Freshman |
| 14 | College Sophomore |
| 15 | College Junior |
| 16 | College Senior |
| 17+ | College Graduate |

#### Overview

### LIX

#### Equation
$LIX = \frac{A}{B} + \frac{C \cdot 100}{A}$

- *A* = Number of Words
- *B* = Number of Periods (defined by period, colon or capital first letter)
- *C* = Number of Long Words (more than 6 letters)

#### Readability Scorecard

| LIX Score Range | Readability Level       |
|------------------|--------------------------|
| &lt; 24             | Very Easy                |
| 25–34            | Easy                     |
| 35–44            | Standard / Medium        |
| 45–54            | Difficult                |
| &gt; 55             | Very Difficult           |


#### Overview

### SMOG (Simple Measure of Gobbledygook)

#### Equation
$grade = \sqrt{PSy \cdot \frac{30}{S}} + 3.1291$

- *PSy* = Number of Polysyllables (Words with 3+ Syllables)
- *S* = Number of Sentences
- *At least 30 sentences needed to accuately score*

#### Readability Scorecard

#### Overview


## Spanish Readability Tests

### Fernandez Huerta Index

#### Equation
$206.835 - (60 \cdot ASL) - (1.02 \cdot ASW)$

#### Readability Scorecard

| Score Range (L) | Readability Level     | U.S. Education Level     | Spain's Education Level    | Age Group           | Reading Grade Level |
|------------------|------------------------|----------------------------|-----------------------------|----------------------|----------------------|
| 101+             | Extremely Easy         | 1st – 3rd Grade            | 1º – 3º Primaria            | 6–8 year olds        | 2.5                  |
| 90 – 100         | Very Easy              | 4th Grade                  | 4º Primaria                 | 9–10 year olds       | 4                    |
| 80 – 89          | Easy                   | 5th Grade                  | 5º Primaria                 | 10–11 year olds      | 5                    |
| 70 – 79          | Somewhat Easy          | 6th Grade                  | 6º Primaria                 | 11–12 year olds      | 6                    |
| 60 – 69          | Average                | 7th – 8th Grade            | 1º – 2º ESO                 | 12–14 year olds      | 7.5                  |
| 50 – 59          | Slightly Difficult     | 9th – 10th Grade           | 3º – 4º ESO                 | 14–16 year olds      | 9.5                  |
| 30 – 49          | Difficult              | 11th – 12th Grade          | 1º – 2º Bachillerato        | 16–18 year olds      | 11.5                 |
| Less than 30     | Extremely Difficult    | College                    | Universidad                 | 18+ year olds        | 13                   |


#### Overview

### The Szigriszt-Pazo Perspicuity Index

#### Equation
$P = 206.835 -62.3 \cdot \frac{Sy}{W} - \frac{W}{S}$

- *P* = Readability Score (Perspicuity Index)
- *Sy* = Total Number of Syllables in the Text
- *W* = Total Number of Words
- *S* = Total number of Sentences

#### Readability Scorecard

| Score (P)     | Reading Level       | U.S. Grade Level     | Age Group         | Reading Ease Score | Spanish Grade Level     |
|---------------|----------------------|------------------------|--------------------|----------------------|---------------------------|
| ≤ 15          | Very Difficult       | College and Above      | 19+ year olds      | 13                   | Universidad               |
| 16 – 35       | Difficult            | 11th – 12th Grade      | 16–18 year olds    | 11.5                 | Bachillerato              |
| 36 – 50       | Slightly Difficult   | 9th – 10th Grade       | 14–16 year olds    | 9.5                  | 3º – 4º ESO               |
| 51 – 65       | Average              | 7th – 8th Grade        | 12–14 year olds    | 7.5                  | 1º – 2º ESO               |
| 66 – 75       | Slightly Easy        | 5th – 6th Grade        | 10–11 year olds    | 5.5                  | 5º – 6º Primaria          |
| 76 – 85       | Easy                 | 3rd – 4th Grade        | 8–9 year olds      | 3.5                  | 3º – 4º Primaria          |
| > 85          | Very Easy            | 1st – 2nd Grade        | 6–7 year olds      | 1.5                  | 1º – 2º Primaria          |


#### Overview

### Gutiérrez de Polini's Readability Formula

#### Equation
$95.2 - 9.7 \cdot \frac{C}{W}- 0.35 \cdot \frac{W}{Snt}$

- *C* = Total Number of Syllables in the Text
- *W* = Total Number of Words
- *Snt* = Total number of Sentences

#### Readability Scorecard

| Gutierrez Interpretation | English Grade          | Age Range         | G Score Range | Spanish Grade Level      |
|--------------------------|-------------------------|--------------------|----------------|----------------------------|
| Very Difficult           | College and Above       | 19+ year olds      | ≤ 20           | Universidad y superior     |
| Difficult                | 11th – 12th Grade       | 16–18 year olds    | ≤ 33           | 1º – 2º Bachillerato        |
| Slightly Difficult       | 9th – 10th Grade        | 14–16 year olds    | ≤ 40           | 3º – 4º ESO                 |
| Average                  | 7th – 8th Grade         | 12–14 year olds    | ≤ 50           | 1º – 2º ESO                 |
| Slightly Easy            | 5th – 6th Grade         | 10–11 year olds    | ≤ 60           | 5º – 6º Primaria            |
| Easy                     | 3rd – 4th Grade         | 8–9 year olds      | ≤ 70           | 3º – 4º Primaria            |
| Very Easy                | 1st – 2nd Grade         | 6–7 year olds      | > 70           | 1º – 2º Primaria            |


#### Overview

## Online Readability Tools

### Grammarly

#### Approach

When a piece of writing is put through Grammarly, Grammarly will make suggestions based on four categories. The categories are **Correctness**, **Clarity**, **Engagement**, and **Delivery**. 

**Correctness** focuses on standard grammar rules such as spelling, punctuation, correct use of homophones, verb tenses, and basic sentence structure.

**Clarity** focusses on sentence length, passive vs. active voice, redundancy, wordiness, and complex or ambiguous wording.

**Engagement** focusses on sentence variety, using specific words in place of general words, avoiding overused words, and tone adjustments.

**Delivery** focusses on matching the tone, formality, and confidence based on who the intended audience and what the intended goal of the text is. This is scaffolded by the "Goals" section of Grammarly, which allows a user to choose what level of knowledge the audience has, what level of formality the tone should be, and what the intent of the writing is.

If you click on the "Overall Score" button, Grammarly displays a "Performance" popup, which includes a "Readability Score" section. They find this score by using the Flesch reading-ease test, which was discussed earlier.

In 2023, Grammarly pivoted to use AI when administering their grammar checks. They have continued to do so up to the present. Before AI, they primarily provided features such as spell checking, rule based grammar errors, punctuation help, plagiarism detection, and citation assistance. After implementing AI, they were able to provide additional features such as tone analysis, content and idea generation, and clarity suggestions. 

The goal of Grammarly is, "To improve lives by improving communication". The company provides many useful services that allows people to improve their writing, including their chrome extension and document analysis tool. It provides tools that helps people improve readability, but their main focus is to help people write better more generally.  

#### Benefits
- Free use with an account (score is available, but some rewriting suggestions are behind a paywall)
- Uses the "Goals" feature to get more context on the goals of the writing, which helps give a more specific grade
- Breaks suggestions into different categories
- Can be utilized both on the website and as an extension (with different features)
- 1-100 scoring is easily understood by people both in and out of the US

#### Limitations
- Signing up for a Grammarly account is required to use the tool
- There is no explicitly stated formula for how Grammarly gets its readability score
- Many useful features are behind a paywall
- Is not entirely focussed on readability, also focussed on engagement
- The explicitly mentioned Readability Score comes from the Flesch readability-ease test, which has flaws that were listed earlier

### LLMs (ChatGPT, Gemini, & Copilot)

#### Approach

Large Language Models can help users make their writing more readable if prompted. The approach  They do so by following this process 

1) Prompt & Text Analysis
2) Determine Heuristic Methodology/Readability Assessment
3) Transformation & Iterative Refinement Process
4) Final Evaluation

A more in depth explanation is that the user 

1) Prompt Analysis
    - A user types in a prompt asking some LLM to make their text more readable
    - The LLM parses and analyzes the prompt, interpreting what the prompt is askin and if there is any additional constraints or context that should be considered
2) Determine Heuristic Methodology/Text Analysis & Readability Assessment
    
3) Transformation & Iterative Refinement Process
4) Final Evaluation

--

1) Understand the Instructions
2) Understand the Text to Manipulate
3) Determine Common Heuristics
4) Plan the Rewrite
5) Generate & Self-Evaluate/Transformation Process/Iterative Refinement
6) Final Evaluation

#### Benefits
- Free to use
- Trained on massive datasets (can simplify well because they have seen lots of writing)
- Can analyze a text based on current, explicit readability tests if prompted
- Can take the context of the writing into account

#### Limitations
- LLMs do not make readability changes based on scores, they do so implicitly
- Prompting limited based on account status

### Hemingway Editor

#### Approach

#### Benefits

#### Limitations

### Rewordify

#### Approach

#### Benefits

#### Limitations

## Overall Analysis

### Similarities

#### Words per Sentence

#### Syllables per Word

#### Scale related to Grade Level

#### Range from 6th grade to College

Almost all of the tools that use grade level for their score index uses 

### Standout Features

#### Common 

## Proposed Readability Test

### Areas to Address

#### Word Familiarity

#### Syntax Complexity

#### Word Similarity between English & Spanish (Cognates)

### Challenges

#### Determining Weights for Variables

#### Lack of Data

### Use Case

#### 