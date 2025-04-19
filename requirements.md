Functional Requirements: 18+ Functions
User Registration - Charlie
A visitor can create an account by providing a username, email, and password.
User Login - Charlie
Registered users can log in using their email and password.
User Logout - Charlie
Logged-in users can log out of their account securely.
Create Recipe - Charlie
Logged-in users can add new recipes with title, description, ingredients, and instructions.
Edit Recipe - Charlie
Users can update their own recipes after creation.
Delete Recipe - Gabriel
Users can delete their own recipes.
View Recipe - Gabriel
Anyone can view the details of a recipe including ingredients and instructions.
Search Recipe - Gabriel
Users can search recipes by title or ingredient keywords.
Rate Recipe - Gabriel
Users can rate a recipe from 1 to 5 stars.
Comment on Recipe - Gabriel
Users can leave comments on a recipe.
View User Profile - Jayden
Users can view their own profile, including their submitted recipes.
Edit User Profile - Jayden
Users can update their display name, email, or password.
Save Recipe (Favorites) - Jayden
Users can save or 'favorite' recipes for quick access later.
View All Recipes - Jayden
Homepage or main recipe list shows all recipes available in the database.
Filter Recipes - Jayden
Users can filter recipes by tags like 'vegan', 'dessert', etc.
Moderate Comments as the Author - Charlie (extra)
Authors can heart, pin, or remove others’ comments on their own recipe pages.
Remix a Saved Recipe - Charlie (extra)
Users repost a recipe created by someone else with modifications, while crediting the original author.
Build a Meal Plan - Charlie (extra)
Users create a personalized meal plan by organizing saved recipes for a specific day or week, such as holiday dinner or weekly meal prep.

Use Case: Example
Name:
Summary:
Actors:
Pre-Conditions:
Trigger:
Primary Sequence:
Alt. Sequence:
Post Condition:

✅1. User Registration
Name
User Registration
Summary
A visitor registers for an account to access the recipe repository
Actor
A potential new user (visitor)
Pre‑Conditions
The visitor is currently on the site
The visitor has navigated to the login page
Trigger
The visitor clicks on “Register Now”
Primary Sequence
The system prompts the visitor to enter a username, password, email address, and display name
System checks if the visitor is an already registered user and validates the inputs
System creates the new account and congratulates the user
Alternate Sequence
The user already exists
System alerts that the username and or email is already in use
System prompts a button that says “Forgot Password?” 
Visitor has the option to edit the input or click to change password
The password does not match the criteria
System alerts the visitor the proper syntax of an accepted password, e.g. length and expected characters 
System prompts to enter a new password
The email address does not exist
System alerts the visitor that the given email address is invalid
System prompts to try again
Given display name has profanity
System detects banned words and alerts the visitor to not use curse words in the name
System prompts to try again
Post‑Conditions
The visitor has a new user account
The new user is now logged in and is shown their new account page
✅2. User Login
Name
User Login
Summary
A registered user logs into their account for the recipe repository
Actors
User
Pre‑Conditions
The user is currently on the site
The user has an existing account
Trigger
The user clicks on the login button
Primary Sequence
The system prompts the user to enter a username, password, and “Remember Me” checkbox
The user enters credentials and can click on the box
System validates the input and logs the user in
Alternate Sequence
The username is invalid
System alerts that the username is wrong
System prompts to try again
The password is invalid
System alerts the visitor the proper syntax of an accepted password, e.g. length and expected characters 
System prompts to try again and a button that says “Forgot Password?” 
Post‑Conditions
The user is authenticated and is logged in
System redirects user to the homepage

✅3. User Logout
Name
User Logout
Summary
A user logs out of their account to end their session securely
Actors
User
Pre‑Conditions
The user is currently logged into their account
Trigger
The user clicks on the “Sign Out” button
Primary Sequence
System receives logout request
System ends user’s session
System clears any authentication tokens and cookies
Alternate Sequence
User is inactive due to long inactivity and session is expired
System logs user out
System displays message like “You’ve been logged out due to inactivity”
Post‑Conditions
System securely logs user out and redirects to the homepage
✅4. Create Recipe
Name
Create Recipe
Summary
A user posts a new recipe to the repository
Actors
User
Pre‑Conditions
The user is currently logged into their account
Trigger
The user clicks on the “Post New Recipe” button
Primary Sequence
System displays a form prompting the user for the required fields: title, ingredients, instructions, and a public/private checkbox, as well as optional extra fields: images, tags, and story
User fills out the required fields and can add on additional optional information
User submits form
System validates and stores recipe into database, linking user as author
System confirms posting of recipe and redirects to a preview of the new recipe page
Alternate Sequence
Missing required fields
System alerts user to complete all required fields
User corrects form and resubmits
Image is not supported
System alerts user that the image is either too large or that the file type is invalid
User retries
Internet or server error
System displays error that the user is offline or site is down
System retains form for a later entry
User tries again when live
Post‑Conditions
New recipe is saved to database
User is redirected to a preview of the new recipe page
✅5. Edit Recipe
Name
Edit Recipe
Summary
A user edits recipes they have previously posted
Actors
User
Pre‑Conditions
The user is currently logged into their account
The user is on their dashboard of posted recipes
Trigger
The user clicks on the “Edit” button for a specific recipe
Primary Sequence
System displays a form pre-filled with the current details for the required fields: title, ingredients, instructions, and a public/private checkbox, as well as optional extra fields: images, tags, and story
User modifies any of the fields and may add on additional optional information
User submits form
System validates and saves changes into database
System confirms posting of recipe and redirects to new preview of the recipe page
Alternate Sequence
Missing required fields
System alerts user to complete all required fields
User corrects form and resubmits
Image is not supported
System alerts user that the image is either too large or that the file type is invalid
User retries
Internet or server error
System displays error that the user is offline or site is down
System retains form for a later entry
User tries again when live
Post‑Conditions
Recipe is updated and saved to database
User is redirected to new preview of the updated recipe page

✅6. Delete Recipe
Name:
Delete Recipe
Summary:
A logged-in user chooses and deletes a recipe that they have created 
Actors:
Primary: Registered User
Pre-Conditions:
The user has already registered an account.
The user is currently authenticated (logged in).
The user has recipes that they have created
Trigger:
User clicks on “Delete Recipe” when viewing a recipe they have created
Primary Sequence:
User selects the recipe they have created
User clicks on the “Delete Recipe” button
System prompts the user with a warning message to confirm deletion
User selects “Yes”
System removes all information of the recipe from the database
Alt. Sequence:
Alt 1: User selects “No”
System prompts the user with a warning message to confirm deletion
User selects “No”
System returns user to recipe view page
Post Condition:
The recipe gets permanently deleted from the database and every user loses access to it
✅7. View Recipe
Name:
View Recipe
Summary:
Logged-in user selects a recipe that they want to view
Actors:
Primary: Registered User
Secondary: Other registered users
Pre-Conditions:
The user has already registered an account.
The user is currently authenticated (logged in).
There are created recipes in the system
Trigger:
User clicks on the title of a recipe 
Primary Sequence:
User clicks on a recipe
System gathers the all information about the recipe 
System redirects user to that recipe page
Alt. Sequence:
Alt 1: No available recipes
User doesn’t have the ability to view recipe
Post Condition:
User is redirected to a recipe page
✅8. Search Recipe
Name:
Search Recipe
Summary:
An user uses the search bar to look for specific recipes that match the search text
Actors:
Primary: Registered User
Primary: System
Pre-Conditions:
The user has already registered an account.
The user is currently authenticated (logged in).
There are created recipes in the system
Trigger:
User types a string in the search bar and clicks on search.
Primary Sequence:
User types in the search bar “apple pie”
System looks through all recipes and returns the ones that match the description
System presents a list with all of recipes that match the search
Alt. Sequence:
Alt 1: No Search Matches
System looks through all recipes and returns the ones that match the description
System returns an error message saying that no recipes were found matching the description
Alt 2: Invalid Search
User types in the search bar only integers or special characters
System returns an error message saying invalid search 
Post Condition:
User is presented with a list of all the recipe that match the search text
✅9. Rate Recipe
Name:
Rate Recipe
Summary:
A logged in user gives a recipe a rating between 1 and 5 starts
Actors:
Primary: User
Pre-Conditions:
The user has already registered an account.
The user is currently authenticated (logged in).
The user is currently inside a recipe’s page
Trigger:
The user selects between 1 and 5 stars
Primary Sequence:
User decides to give a the recipe a rating of 5 stars
The user clicks on the 5th star
System updates the rating of the recipe
System saves the user that gave the rating to the recipe on the recipe’s profile
Alt. Sequence:
Alt 1: User doesn’t leave a rating
User leaves the recipe page without giving a rating
Post Condition:
The rating value for a recipe gets updated in the database, and all other users can see the new rating
✅10. Comment on Recipe
Name:
Comment on Recipe
Summary:
A logged in user types out and leaves a comment under a recipe page
Actors:
Primary: User
Pre-Conditions:
The user has already registered an account.
The user is currently authenticated (logged in).
The user is currently inside a recipe’s page
Trigger:
User goes to the comment section and clicks on “Leave a Comment”
Primary Sequence:
User clicks on “Leave a Comment”
User types out the comment on a 250 characters limit
User submits the comment
System adds the comment to the recipe page
System shows the comment on the comment section of the recipe page
Alt. Sequence:
Alt 1: Empty Comment
User doesn’t type anything on the comment body
User clicks submit
System prompts an error message stating that the comment is empty
Alt 2: Over the Character Limit
User types a comment that goes over the 250 character limit
System prompts an error stating that the comment is over the character limit
System returns User to their comment
Post Condition:
The comment is added to the comment section of the recipe page and is available for all users to see
✅11. View User Profile
Name: 
View User Profile
Summary: 
A logged‑in user can view their profile page, which displays personal information (display name, email), account settings, and a list of recipes they have submitted.
Actors:
Primary: Registered User
Pre‑Conditions:
The user has already registered an account.
The user is currently authenticated (logged in).
Trigger:
The user clicks or taps the “My Profile” button in the site header or navigation menu.
Primary Sequence
User selects “My Profile.”
System retrieves the user’s profile data (display name, email, registration date) and their submitted recipes from the database.
System renders the Profile page, showing:
User’s display name and email
List of submitted recipes (titles with links)
Buttons/links for editing profile or logging out
User views their information and can select any listed recipe to view its details.
Alternate Sequences
Alt. 1: No Submitted Recipes
User selects “My Profile.”
System retrieves the user’s profile data (display name, email, registration date) and their submitted recipes from the database.
User’s recipe list query returns empty.
System displays a placeholder message: “[User] hasn’t submitted any recipes yet.”
Post‑Conditions:
The user is presented with an up‑to‑date view of their profile and can navigate to edit settings or review their recipes.


✅12. Edit User Profile
Name: Edit User Profile
Summary: 
Allows a logged‑in user to update their display name, email address, and/or password securely.
Actors:
Primary: Registered User
Pre‑Conditions:
The user has already registered an account.
The user is currently authenticated (logged in).
Trigger:
User clicks the “Edit Profile” button or link on their profile page.
Primary Sequence
System displays the Edit Profile form populated with the user’s current display name and email (password fields blank).
User modifies one or more of the following fields:
Display Name
Email Address
Password 
If changing password, user enters:
Current password
New password
New password confirmation
User submits the form.
System validates inputs:
Display Name: non‑empty, within length limits
Email: correct format, not already in use by another account
If password change requested: current password matches, new ≠ current, meets complexity rules, confirmation matches
On successful validation, system updates the user record in the database.
Alternate Sequences
Alt. 1: Invalid Display Name or Email Format
System highlights invalid fields, displays error messages (“Name cannot be blank,” “Invalid email format”), and returns to Step 2.
Alt. 2: Email Already In Use
System displays “Email is already registered” error, prompts user to enter a different email, then returns to Step 2.
Alt. 3: Incorrect Current Password (when changing password)
System displays “Current password is incorrect,” clears password fields, and returns to Step 2.
Post‑Conditions:
User’s profile (display name, email, and/or password) is updated in the system.
✅13. Save Recipe (Favorites)
Name: 
Save Recipe (Favorites)
Summary: 
Allows a logged‑in user to mark a recipe as a favorite (“save” it) for quick access later, and to remove it from their favorites list.
Actors:
Primary: Registered User
Pre‑Conditions:
The user has already registered an account.
The user is currently authenticated (logged in).
Trigger:
User clicks the “Add to Favorites” button on a recipe listing or detail page.
Primary Sequence
User clicks the “Save” control on a recipe.
Server verifies authentication and confirms the recipe exists.
Server checks for an existing favorite record for (userId, recipeId).
Server responds with success and the updated favorite state (favorited: true).
Client updates the UI (e.g., fills the heart icon).
Alternate Sequences
Alt. 1: Remove Favorite
User clicks the filled heart (“Unsave”).
Server verifies authentication, locates and deletes the favorite record.
Server returns success with favorited: false.
Client toggles the UI back to an empty heart.
Post‑Conditions:
On Save: A record linking the user to the recipe exists in the Favorites table.
UI reflects the current favorite status consistently across the site.




✅14. View All Recipes
Name: 
View All Recipes
Summary: 
Allows any visitor or logged‑in user to browse a paginated list of all recipes stored in the system, with basic details (title, author, thumbnail, average rating).
Actors:
Primary: Registered User
Secondary: Other Registered Users
Pre‑Conditions:
The user has already registered an account.
The user is currently authenticated (logged in).
Trigger:
User navigates to the “All Recipes” page.
Primary Sequence
User selects “View All Recipes.”
Server retrieves the requested page of recipes from the database, including:
Recipe ID
Title
Author/display name
Client renders the list in a grid or list view, showing the basic details for each recipe.
If more recipes are available beyond the current page, client displays pagination controls (“Next”, “Previous”) or infinite‑scroll loader.
User can click on any recipe to view its full details.
Alternate Sequences
Alt. 1: No Recipes Found
Server returns an empty list.
Client displays a friendly message: “No recipes found. Be the first to add one!”
Post‑Conditions:
A page of recipes is displayed to the user.
No changes are made to the database (read‑only operation).






✅15. Filter Recipes
Name: 
Filter Recipes
Summary: 
Allows any visitor or logged‑in user to narrow down the recipe list by applying one or more criteria—such as tags (e.g., “vegan,” “dessert”), ingredient keywords, or author—so they can quickly find recipes matching their preferences.
Actors:
Primary: Registered User
Secondary: Other Registered Users
Pre‑Conditions:
The user has already registered an account.
The user is currently authenticated (logged in).
Trigger:
User interacts with the filter controls (e.g., selects tag checkboxes, enters an ingredient keyword, or chooses an author) on the recipe listing page.
Primary Sequence
User opens the filter panel or form on the recipes page.
User selects one or more filter options:
Tags (multi‑select)
Ingredient keywords (free‑text search)
Author (dropdown or autocomplete)
User clicks “Apply Filters” (or filters are applied dynamically as selections change).
Server validates and parses filter parameters.
Server queries the database, applying WHERE clauses or full‑text search to return only recipes matching all active filters.
Server returns a paginated JSON response containing the filtered recipes and updated pagination metadata.
Client renders the filtered list and updates pagination controls accordingly.
Alternate Sequences
Alt. 1: No Recipes Match Filters
Server returns an empty list.
Client displays a friendly message: “No recipes match your filters—try broadening your search.”
Post‑Conditions:
The recipe listing reflects only those recipes that satisfy the applied filters.
Pagination and sorting remain consistent with any filter constraints.





✅16. Moderate Comments as the Author
Name
Moderate Comments as the Author
Summary
Authors can heart (like), pin, or remove others’ comments on their own recipe pages
Actors
Author (user)
commenters (other users)
Pre‑Conditions
The user is currently logged into their account
The user is on their dashboard of posted recipes
The user is viewing the comment section of a specific recipe page
Trigger
The author clicks and holds on a comment
Primary Sequence
System displays a prompt to either heart (like), pin, or remove the comment
User chooses one
System receives request and saves changes into database
For removals, system prompts for reason, e.g. unprovoked hate, etc.
System alerts commenters of author’s action on their comment
System updates and shows new view of the updated comment section
Alternate Sequence
Profanity in comments
System detects profane language used in comment
System automatically deletes comment and alerts commenter
System updates comment section
Comment does not exist
System alerts author that the comment they’re trying to moderate has already been deleted
System shows updated comment section
Post‑Conditions
Comment section is updated and saved to database
User is redirected to updated view of the comment section









✅17. Remix a Saved Recipe
Name
Remix a Saved Recipe
Summary
Users can repost and modify a recipe created by someone else, while crediting the original author
Actors
User
Pre‑Conditions
The user is currently logged into their account
The user is viewing a recipe page of another user
Trigger
The user clicks on the remix/clone button
Primary Sequence
System receives request and shows a form pre-filled with the current details for the required fields: title, ingredients, instructions, and a public/private checkbox, as well as optional extra fields: images, tags, and story
The user modifies any of the fields, and system automatically has a field that credits the original recipe and author
User submits form
System validates and updates remixed recipe into database
System updates and shows preview of recipe page
Alternate Sequence
Missing required fields
System alerts user to complete all required fields
User corrects form and resubmits
Image is not supported
System alerts user that the image is either too large or that the file type is invalid
User retries
Internet or server error
System displays error that the user is offline or site is down
System retains form for a later entry
User tries again when live
Post‑Conditions
Recipe is remixed and saved to database with credit to the original author
User is redirected to new preview of the remixed recipe page






✅18. Build a Meal Plan
Name
Build a meal plan
Summary
Users create a personalized meal plan by organizing saved recipes for a specific day or week, such as holiday dinner or weekly meal prep
Actors
User
Pre‑Conditions
The user is currently logged into their account
The user is viewing their dashboard of saved recipes
Trigger
The user clicks on the “Create Meal Plan” button
Primary Sequence
System prompts user to select a date or a range of dates
User chooses certain saved recipes and assign them tags, e.g. breakfast, lunch, dinner, snacks, etc., for each day(s)
The user adds a title, e.g. “Christmas Dinner Plan” or “Week 1 Meal Prep”, and optional notes, e.g. “diet for the week”
User submits meal plan form
System saves meal plan into database and links it to the user
System confirms plan has been saved and redirects user to new preview of the meal plan
Alternate Sequence
No recipes selected
System alerts user to select at least one recipe for the plan
User selects and resubmits
Invalid date range
System alerts user to choose a valid day or date range
User updates selection
Internet or server error
System displays error that the user is offline or site is down
System retains form for a later entry
User tries again when live
Post‑Conditions
System saves meal plan to the database and links it to the user’s account
User is redirected to preview of the new meal plan