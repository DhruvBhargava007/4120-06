import pandas as pd
from scipy import stats
import numpy as np

# Data: Time to send a message (in seconds)
# Participants who saw embedded chat first
group1_embedded = [7.15, 5.46, 7.51]
group1_hidden = [6.3, 4.43, 4.73]

# Participants who saw hidden chat first
group2_hidden = [8.83, 10.21, 10.50]
group2_embedded = [4.26, 8.76, 6.39]

# Combine into independent samples (each participant used both, but we treat groups as independent here)
embedded_times = group1_embedded + group2_embedded
hidden_times = group1_hidden + group2_hidden

# Self-reported ease of use: all preferred embedded, coded as 5 for embedded, 1 for hidden for Mann-Whitney
embedded_ratings = [5, 5, 5, 5, 5, 5]
hidden_ratings = [1, 1, 1, 1, 1, 1]

# Shapiro-Wilk test for normality (assumption check)
shapiro_embedded = stats.shapiro(embedded_times)
shapiro_hidden = stats.shapiro(hidden_times)

# Chi-squared test is not appropriate for continuous data, so we proceed with non-parametric Mann-Whitney U test
mann_whitney_time = stats.mannwhitneyu(embedded_times, hidden_times, alternative='two-sided')

# Mann-Whitney U test for ease of use ratings
mann_whitney_ratings = stats.mannwhitneyu(embedded_ratings, hidden_ratings, alternative='two-sided')

# Collect results
{
    "Shapiro-Wilk Embedded": shapiro_embedded,
    "Shapiro-Wilk Hidden": shapiro_hidden,
    "Mann-Whitney U (Time)": mann_whitney_time,
    "Mann-Whitney U (Ease of Use)": mann_whitney_ratings
}

