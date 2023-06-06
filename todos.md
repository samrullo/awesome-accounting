# TODO ideas

## Primary function
Primary function of this app is to provide accounting capabilities to the business owner.
Business owner should be able to 
- record revenues
- record expenses
- view accounting statements such as income statement, balance sheet

## User type maintenance
Better to have Child as a user. Hesitating between changing User model to have user type such as child, parent, teacher vs having separate tables for each user type

## Additional features
- Would be great if potentially children or parents could log into the platform and check upcoming schedules about courses to which they are subscribed. Or check what were homeworks for a given course.
- Would be great to have a calendar where important events are marked. And everybody (parents, teachers, staff) can check them out

## Multi language support
I want the platform to support multiple languages like
- English
- Russian
- Japanese
I am not yet sure how I am going to implement it. One idea was leverage GPT to translate everything in html files and files and then store translations in some data structure and use them

## Embed Language Model
It would be cool if the user could interact with the platform using natural language.
For example, user could type "build rental for next year hundred thousand yens", and the platform could record that info in structured format into appropriate sql tables.