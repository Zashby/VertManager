
# Vertical Farm management application

## Project Overview
Urban development and growing population centers have necessitated the development of space-conscious production plants to produce agricultural products at an accelerated rate and with less of a need for long-distance transportation. Vertical farms, such as Kalera, Vertical Roots, Cornucopia Farms, etc..., require constant attention and monitoring to produce a viable product. However, many companies have leaped onto commercial opportunity without creating the simple tools which would make the task of maintaining products to contractual standards easy. 

My wife works at a vertical farm in Georgia and regularly talks about the failings of her company's production model. One side of this is the lack of proper tools for the horticultural team to use in ensuring all maintenance and tasks are completed to standard. Currently, a "spaghetti-coded" excel document is what the entire team uses over a shared server which suffers from frequent formatting errors and generally looks like a complete mess. My goal is to to build up something easier to understand to implement for usage by the team. I have, for the record, no illusions that this product will ever be used by a major company, but it was a niche product I felt I could produce with real world consulation from a prospective user. 

**TL;DR; My wife works at a vertical farm which uses a janky excel farm tracking document for a large-scale operation. I want to make a better one. 

## Functionality
**Primary goals**
- Establish farm heirarchy 
   - Zones (12 for test build)
    - Stacks (9 per zone)
- Track farm maintenance logs and lifecycle information
  - Lettuce by broad type
    - Affects light schedule for zones
  - Track scouting logs and requirements
    - One scout per stack per 7 day cycle. Four times.
    - Harvest times
      - Whole head: 28 days
      - loose Leaf: 21 days
  - Calibrate equipment
    - Every zone. Stacks 2, 5, and 8. Monthly 
- Easy color scheme for recognizing maintenance issues and scouting/tracking requirements.
  - Black out empty zones, stacks, and towers.

**Secondary Goals**
- Ability to deploy and track individual farm sites with relatively simple scalability
- Harvest forecasting
- Specific lettuce species logging
  - Searching for suitable API to pull information regarding specific plants for reference material on hand
- Easy signature system for employees to sign off on tracking and maintenance logs
- Make this junk reactive
- Track farm employees
  - Site
  - Position
  - Signature
  - Schedule / taskings
- Add employees page (would probably actually be an admin task for a company, but might as well make it look nice)


## Data Model

#### Farm
  - id
  - name
  - Location
  - Employees
  - Zones

#### Employees / Users
  - Name
  - Password
  - Position / Job Title / user-permissions(Stretch)
  - Employee location

#### Zones
  - Zone ID
  - Product type (for light scheduling later)
  - Stacks (ManytoManyField)

#### Stacks
  - Stack ID (include zone number in stack ID)
  - Scout Log
    - Date tracker
  - Harvest Schedule
    -Date tracker / Some boolean check
  - Calibration log (2, 5, and 8)
  - (stretch) Harvest forecast specific information

## Schedule

- Week 1 - Make initial farm heriarchy models
  - [ ] Ensure proper data types chosen for all input fields
  - [ ] Create models
    - [ ] User (no special work will be implemented for users here)
    - [ ] farm/zones/stacks
    - [ ] Proper date tracking
  - [ ] Develop test/temporary UI for reading information (simple grid layout for ease of creation)
  - [ ] End of week create a new branch save for safety
- Week 2 - Start working on user input
  - [ ] Tracking logs
    - [ ] Ensure app properly updates dates for scouting / maintenance and proper system response
  - [ ] login / signout page
  - [ ] If things are going well, update user model to reflect position
  - [ ] Framework final UI 
  - [ ] Work on Light Schedule tracking page
  - [ ] Assess ability to implement stretch goals
  - [ ] Ask wife if I messed anything up so far
  - [ ] End of week create a new branch save for safety
- Week 3 - Work on Final UI build
  - [ ] create an overall theme/color pallet (thinking some kinda green and white color scheme, but we'll see )
  - [ ] walk through typical user flow to check for any bugs
    - [ ] Fix any bugs that may pop up
  - [ ] Have a presentation ready project
  - [ ] End of week create a new branch save for safety
- Week 4 - 
- [ ] Cry about my horrible color choice / style for a bit
- [ ] Last minute error checking, probably get some other people to try to break the app for me
- [ ] Think about worthwhile talking points for presentation
- [ ] Day before presentation make a new branch save for safety
- Week 5 and beyond!
- [ ] Realize I should have just worked on the DnD / boardgame local group finder app instead
- [ ] Assess implementation of secondary goals and ability to create new farms in app
- [ ] Find somewhere to deploy this app through since Heroku hates free people
- [ ] Have a good lie down