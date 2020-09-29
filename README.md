CS50x’s Web Programming with Python and JavaScript
Capstone (July 2020 Version)

GitHub: Tim9N

Multiple Intelligence Website:

Background:
The theory of multiple intelligences differentiates human intelligence into specific 'modalities', rather than
seeing intelligence as dominated by a single general ability. Howard Gardner proposed this model in his 1983
book Frames of Mind: The Theory of Multiple Intelligences. Examples of intelligence 'modalities' are musical-rhythmic,
visual-spatial, verbal-linguistic, logical-mathematical, bodily-kinesthetic, interpersonal, intrapersonal, and
naturalistic. In essence, these 'modalities' can be used to determine how a person's most effective learning takes place.

Purpose:
Allow teachers to determine how their students learn best.

Uses:
If schools continue to be online, teachers can use this test to seperate their students into
groups based on how they learn best. The teacher can then meet with these groups seperatly and give assignments
that best align with the students' learning style.

Functionality:
    Users: Using Django models, teachers can sign up for accounts and create classes for their students. Users also have the    ability to log in and log out. 
    Classes: Using Django models, user-created classes allow for the grouping of students' results. Each class has a unique code for students to use when taking the test.
    Test: The website includes a standardized version of the Multiple Intelligence Test. Teachers can share their custom links or codes to their classes and have students take the test. Using Javascript, codes are sycronslly verified. On submission, Javascipt is used to check all inputs and verify that they are valid. Results are generated for the test-taker and, if part of a class, results will be added to a Django model for teachers to view. Rather than having the test questions hard coded, using Django, questions are loaded into the template automatically. 
    Dashboard: For teachers, the dashboard is the main page. Teachers can create and view their classes. Each class lists its code and students' results. Using Ajax and Django, results are compiled into doughnut graphs to easily see the top categories. Using Javascript, custom links for each class are created and can be copied to the user's clipboard. 

Distinctiveness:
While the User management part of the website is similar to prior projects, the rest of the project has no similar ascpects to other projects. This projcet is mainly a test taking and data management project compared to more posts-based projects like the ones in this course. 

Complexity:
This project is fairly more complex than other projects in this course due to its extensive use of Djano and Javascript. As mentioend in the Functionality section, this website uses Django to dynamically load pages, manage data, and organize requests. Javasciprt and Ajax are used to syconrolsally verify data and add dynamic elements into the page. One of the more complex pieces of this project is the dynamic generation of graphs that display data in real-time.