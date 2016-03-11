## 1. Load data from csvs
import unicodecsv

def read_csv(filename):
  with open(filename, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    return list(reader)

enrollments = read_csv("enrollments.csv")
daily_engagement = read_csv('daily_engagement.csv')
project_submissions = read_csv('project_submissions.csv')

print enrollments[0]
print daily_engagement[0]
print project_submissions[0]

## 2. Fix data types
from datetime import datetime as dt

# Takes a date as a string and returns a Python datetime object
def parse_date(date):
  if data == '':
    return None
  else:
    return dt.strptime(date, '%Y-%m-%d')

# Takes a string which is either an empty string or represents an integer, and returns an int
def parse_maybe_int(i):
  if i == '':
    return None
  else:
    return int(i)

# Clean up the data types in the enrollments table
for enrollment in enrollments:
  enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
  enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
  enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
  enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
  enrollment['join_date'] = parse_date(enrollment['join_date'])

enrollments[0]

# Clean up the data types in the engagement table
for engagement_record in daily_engagement:
  engagement_record['lessons_completed'] = int(float(engagement_record['lessons_completed']))
  engagement_record['num_courses_visited'] = int(float(engagement_record['num_courses_visited']))
  engagement_record['projects_completed'] = int(float(engagement_record['projects_completed']))
  engagement_record['total_minutes_visited'] = float(engagement_record['total_minutes_visited'])
  engagement_record['utc_date'] = parse_date(engagement_record['utc_date'])
    
daily_engagement[0]

# Clean up the data types in the submissions table
for submission in project_submissions:
  submission['completion_date'] = parse_date(submission['completion_date'])
  submission['creation_date'] = parse_date(submission['creation_date'])

project_submissions[0]

# Investigate the data
# Find the total number of rows in each table
def row_count(filename):
  row_num = sum(1 for row in filename)
  return row_num

print row_count(enrollments)
# OR
len(enrollments)

# Rename the "acct" column in the daily_engagement table to "account_key"
for record in daily_engagement:
  record['account_key'] = record.pop['acct']

daily_engagement[0]

# Find the # of unique students (account keys) in each table
def student_count(filename):
  unique_students = set()
  for row in filename:
    unique_students.add(row['account_key'])
  return unique_students

print len(student_count(enrollments))
print len(student_count(daily_engagement))
print len(student_count(project_submissions))

# Find any one student enrollments where the student is missing from the daily engagement table
engagement_unique_students = student_count(daily_engagement）

for enrollment in enrollments:
  student = enrollment['account_key']
  if student not in engagement_unique_students:
    print enrollment
    break

# Check for more problem records
num_problem = 0
for row in enrollments:
  student = enrollment['account_key']
  if student not in engagement_unique_students and enrollment['days_to_cancel']!=0:
    num_problem += 1
    
print num_problem

# Create a set of the account keys for all Udacity test accounts
udacity_test_accounts = set()

for row in enrollments:
  if row['is_udacity']:
    udacity_test_accounts.add(row['account_key'])

len(udacity_test_accounts)

# Given some data with an account_key field, removes any records corresponding to Udacity test accounts
def remove_test_accounts(filename):
  non_udacity_data = []
  for row in filename:
    if row['account_key'] not in udacity_test_accounts:
      non_udacity_data.append(row)
  return non_udacity_data

# Remove test accounts from all three tables
non_udacity_enrollments = remove_udacity_accounts(enrollments)
non_udacity_engagement = remove_udacity_accounts(daily_engagement)
non_udacity_submissions = remove_udacity_accounts(project_submissions)

print len(non_udacity_enrollments)
print len(non_udacity_engagement)
print len(non_udacity_submissions)

# Create a dictionary named paid_students containing all students who either
# haven't canceled yet or who remained enrolled for more than 7 days. The keys
# should be account keys, and the values should be the date the student enrolled
paid_students = {}

for student in non_udacity_enrollments:
  if not student['is_canceled'] or student['days_to_cancel'] > 7:
    account_key = student['account_key']
    enrollment_date = student['join_date']
    if account_key not in paid_students:
      paid_students[account_key] = enrollment_date

print paid_students.iteritems().next()

