from scipy import stats

# Time to send message (6 participants, 2 interface types)
group1_embedded = [7.15, 5.46, 7.51]
group1_hidden = [6.3, 4.43, 4.73]
group2_hidden = [8.83, 10.21, 10.50]
group2_embedded = [4.26, 8.76, 6.39]

embedded_times = group1_embedded + group2_embedded
hidden_times = group1_hidden + group2_hidden

# Ease of use ratings (all preferred embedded)
embedded_ratings = [5, 5, 5, 5, 5, 5]
hidden_ratings = [1, 1, 1, 1, 1, 1]

# Shapiro-Wilk Test for normality
stats.shapiro(embedded_times)
stats.shapiro(hidden_times)

# Mann-Whitney U Tests
stats.mannwhitneyu(embedded_times, hidden_times, alternative='two-sided')
stats.mannwhitneyu(embedded_ratings, hidden_ratings, alternative='two-sided')
