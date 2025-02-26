import re

sentiment_analysis ="Unfortunately one of those moments wasn't a giant squid monster. User_mentions:2, likes: 9, number of retweets: 7"
# Write a regex to obtain user mentions
print(re.findall(r"User_mentions:\d", sentiment_analysis))
# Write a regex to obtain number of likes
print(re.findall(r"likes:\s\d", sentiment_analysis))
# Write a regex to obtain number of retweets
print(re.findall(r"number\sof\sretweets:\s\d", sentiment_analysis))

sentiment_analysis = 'He#newHis%newTin love with$newPscrappy. #8break%He is&newYmissing him@newLalready'
# Write a regex to match pattern separating sentences
regex_sentence = r"\W\dbreak\W"

# Replace the regex_sentence with a space
sentiment_sub = re.sub(regex_sentence, " ", sentiment_analysis)

# Write a regex to match pattern separating words
regex_words = r"\Wnew\w"

# Replace the regex_words and print the result
sentiment_final = re.sub(regex_words, " ", sentiment_sub)
print(sentiment_final)

# new sentiment_analysis
# 545    Boredd. Colddd @blueKnight39 Internet keeps st...
# 546    I had a horrible nightmare last night @anitaLo...
# 547    im lonely  keep me company @YourBestCompany! @...
# Name: text, dtype: object
sentiment_analysis = ['Boredd. Colddd @blueKnight39 Internet keeps shutting down. Such a nightmare! @anitaLopez98 Same here @YourBestCompany! I am lonely', 'I am sooo happy @blueKnight39. Great concert @anitaLopez98 @YourBestCompany']
for tweet in sentiment_analysis:
	# Write regex to match http links and print out result
    print(re.findall(r"http\S+", tweet))

    # Write regex to match user mentions and print out result
    print(re.findall(r"@\w+\d+", tweet))

# Complete the for-loop with a regex that finds all dates in a format similar to 27 minutes ago or 4 hours ago.
for date in sentiment_analysis:
	# print(re.findall(r"\d{____}\s____\s____", date))
    print(re.findall(r"\d{1,2}\s\w+\sago", date))

# Complete the for-loop with a regex that finds all dates in a format similar to 23rd june 2018.
for date in sentiment_analysis:
    # 	print(re.____(r"____{____}____\s____\s____{____}", date))
    print(re.findall(r"\d{1,2}\w+\s\w+\s\d{4}", date))

# Complete the for-loop with a regex that finds all dates in a format similar to 1st september 2019 17:25.
for date in sentiment_analysis:	
    # print(re.____(r"____{____}____\s____\s____{____}\s____{____}:____{____}", date)) 
    print(re.findall(r"\d{1,2}\w+\s\w+\s\d{4}\s\d{1,2}:\d{2}", date))

# Write a regex matching the hashtag pattern
regex = r"#\w+"

# Replace the regex by an empty string
no_hashtag = re.sub(regex, "", sentiment_analysis)

# Get tokens by splitting text
print(re.split(r"\s+", no_hashtag))

# Write a regex to match text file name
# regex = r"_[_]{_}_txt"
regex = r"_[a-z0-9]+\.txt"


# for text in sentiment_analysis:
# 	# Find all matches of the regex
# 	# print(re.____(____, ____))
#     print(re.findall(regex, text))
    
# 	# Replace all matches with empty string
# 	print(re.____(____, ____, ____))

# Sample email list for testing
emails = ['n.john.smith@gmail.com', 'jane_doe12@yahoo.com', '!#%$&*@company.com', 'my@email.com', 'invalid.com', '@invalid.com']

# Write a regex to match a valid email address
regex = r"[A-Za-z0-9!#%&*$\.]+@\w+\.com"

for example in emails:
    # Match the regex to the string
    if re.match(regex, example):
        # Complete the format method to print out the result
        print("The email {email_example} is a valid email".format(email_example=example))
    else:
        print("The email {email_example} is invalid".format(email_example=example))

# Sample password list for testing
passwords = ['Apple34!rose', 'My87hou#4$', 'abc123', 'longer_password123456']

# Write a regex to check if the password is valid
regex = r"[A-Za-z0-9*#$%!&\.]{8,20}"

for example in passwords:
    # Scan the strings to find a match
    if re.match(regex, example):
        # Complete the format method to print out the result
        print("The password {pass_example} is a valid password".format(pass_example=example))
    else:
        print("The password {pass_example} is invalid".format(pass_example=example))

string = 'I want to see that <strong>amazing show</strong> again!'
# Write a regex to eliminate tags
string_notags = re.sub(r"<.+?>", "", string)

sentiment_analysis = 'Was intending to finish editing my 536-page novel manuscript tonight, but that will probably not happen. And only 12 pages are left '
# Write a lazy regex expression 
numbers_found_lazy = re.findall(r"\d+?", sentiment_analysis)

# Write a greedy regex expression 
numbers_found_greedy = re.findall(r"\d+", sentiment_analysis)

sentiment_analysis = "Put vacation photos online (They were so cute) a few yrs ago. PC crashed, and now I forget the name of the site (I'm crying). "

# Write a greedy regex expression to match 
sentences_found_greedy = re.findall(r"\(.+\)", sentiment_analysis)

# Write a lazy regex expression
sentences_found_lazy = re.findall(r"\(.+?\)", sentiment_analysis)

sentiment_analysis = ['Just got ur newsletter, those fares really are unbelievable. Write to statravelAU@gmail.com or statravelpo@hotmail.com. They have amazing prices',
 'I should have paid more attention when we covered photoshop in my webpage design class in undergrad. Contact me Hollywoodheat34@msn.net.',
 'hey missed ya at the meeting. Read your email! msdrama098@hotmail.com']

# Write a regex that matches email
regex_email = r"\S+@\S+"

for tweet in sentiment_analysis:
    # Find all matches of regex in each tweet
    email_matched = re.findall(regex_email, tweet)
    
    # Complete the format method to print the results
    print("Lists of users found in this tweet: {}".format(email_matched))

# You need to extract the information about the flight:

#     The two letters indicate the airline (e.g LA),
#     The 4 numbers are the flight number (e.g. 4214).
#     The three letters correspond to the departure (e.g AER),
#     The destination (CDB),
#     The date (06NOV) of the flight.

# write regex to capture important information about the flight
flight = 'Subject: You are now ready to fly. Here you have your boarding pass IB3723 AMS-MAD 06OCT'

# Write regex to capture information of the flight
regex = r"([A-Z]{2})(\d{4})\s([A-Z]{3})-([A-Z]{3})\s(\d{2}[A-Z]{3})"

# Find all matches of the flight information
flight_matches = re.findall(regex, flight)

#Print the matches
print("Airline: {} Flight number: {}".format(flight_matches[0][0], flight_matches[0][1]))
print("Departure: {} Destination: {}".format(flight_matches[0][2], flight_matches[0][3]))
print("Date: {}".format(flight_matches[0][4]))

sentiment_analysis = ['I totally love the concert The Book of Souls World Tour. It kinda amazing!',
 'I enjoy the movie Wreck-It Ralph. I watched with my boyfriend.',
 "I still like the movie Wish Upon a Star. Too bad Disney doesn't show it anymore."]

# Write a regex that matches sentences with the optional words
regex_positive = r"(love|like|enjoy).+?(movie|concert)\s(.+?)\."

for tweet in sentiment_analysis:
    # Find all matches of regex in tweet
    positive_matches = re.findall(regex_positive, tweet)
    
    # Complete format to print out the results
    print("Positive comments found {}".format(positive_matches))

# Write a regex that matches sentences with the optional words
regex_negative = r"(hate|dislike|disapprove).+?(?:movie|concert)\s(.+?)\."

for tweet in sentiment_analysis:
    # Find all matches of regex in tweet
    negative_matches = re.findall(regex_negative, tweet)
    
    # Complete format to print out the results
    print("Negative comments found {}".format(negative_matches))

contract = 'Provider will invoice Client for Services performed within 30 days of performance.  Client will pay Provider as set forth in each Statement of Work within 30 days of receipt and acceptance of such invoice. It is understood that payments to Provider for services rendered shall be made in full as agreed, without any deductions for taxes of any kind whatsoever, in conformity with Provider’s status as an independent contractor. Signed on 03/25/2001.'

# Write regex and scan contract to capture the dates described
regex_dates = r"Signed\son\s(\d{2})/(\d{2})/(\d{4})"
dates = re.search(regex_dates, contract)

# Assign to each key the corresponding match
signature = {
    "day": dates.group(2),
    "month": dates.group(1),
    "year": dates.group(3)
}

# Complete the format method to print-out
# print("Our first contract is dated back to {data[____]}. Particularly, the day {data[____]} of the month {data[____]}.".format(data=____))
print("Our first contract is dated back to {data[year]}. Particularly, the day {data[day]} of the month {data[month]}.".format(data=signature))

html_tags = ['<body>Welcome to our course! It would be an awesome experience</body>',
 '<article>To be a data scientist, you need to have knowledge in statistics and mathematics</article>',
 '<nav>About me Links Contact me!']

for string in html_tags:
    # Complete the regex and find if it matches a closed HTML tags
    match_tag =  re.match(r"<(\w+)>.*?</\1>", string)

    if match_tag:
        # If it matches print the whole tag
        print("Your tag {} is a closed HTML tag".format(match_tag.group()))
    else:
        # If it doesn't match capture only the tag 
        notmatch_tag = re.match(r"<(\w+)>", string)
        # Print only the tag
        print("Close your {} tag!".format(notmatch_tag.group()))

# Complete the regex to match an elongated word
regex_elongated = r"\w*(\w)\1\w*"

for tweet in sentiment_analysis:
	# Find if there is a match in each tweet 
    match_elongated = re.search(regex_elongated, tweet)
    
    # Complete the format method to print the result
    if match_elongated:
        print("Elongated word found: {word}".format(word=match_elongated.group()))
    else:
        print("No elongated word found")

sentiment_analysis = "You need excellent python skills to be a data scientist. Must be! Excellent python"

# Positive lookahead
look_ahead = re.findall(r"\w+(?=\spython)", sentiment_analysis)

# Print out
print(look_ahead)

# Positive lookbehind
look_behind = re.findall(r"(?<=\s)python\s\w+", sentiment_analysis)

# Print out
print(look_behind)

cellphones = ['4564-646464-01', '345-5785-544245', '6476-579052-01']

for phone in cellphones:
    # Get all phone numbers not preceded by area code
    number = re.findall(r"(?<!\d{3}-)\d{4}-\d{6}-\d{2}", phone)
    print(number)

for phone in cellphones:
    # Get all phone numbers not followed by optional extension
    number = re.findall(r"\d{3}-\d{4}-\d{6}(?!-\d{2})", phone)
    print(number)