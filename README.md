

User Docs/Developer Docs are being created Project is currently messy but should be fixed in the future.


*This doc will be added to as more progress is made on the project*
Language Identification of Vocal Lyrics in Songs
Russell Brown
Taylor LeBlond
Christopher Lam

Algorithm Coordinator
RussellRok@gmail.com

Music Database Manager
wtleblond@gmail.com

Music Data Analyst
chris_lam25@hotmail.com

*Music Database Not Stored Online due to Copyright issues*
*If you wish to know the database used feel free to message the group*

Project Idea
This goal of this project is to be able to isolate the vocals of a song and identify the language in which a song is being sung. The song will be inputted by using a microphone or sent in as an audio file. 

INTRODUCTION
The goal of this project is to create a program to determine which language is being sung in a song. The song will be played through a microphone or sent in as a file and the program will then compare the newly read in song against the musical database and return which language matches the currently sung language, as well as the statistical likeliness of all the other languages. The statistical likeliness can be accomplished in multiple ways in order to determine which is the most accurate at interpreting the language of the song.

METHODS OF ANALYSIS
One way in which the language can be determined will be by isolating the vocal track. By using vocal isolation, it would be by reducing the amount of non-vocal background noise. In doing so, it allows the isolated track to be easily compared to a track of a known language in the database. More methods will be explored later, but this will most likely be the most effective analysis method.

DATABASE INFORMATION
The database of languages will consist of English, French, German and Japanese. More languages may be added later, but these four will be the starting point. To begin testing, there will be a compilation of approximately 400 songs. The end goal will be to have a 90% accuracy with the 4 main languages. Due to the vast amount of genres of music, the genres of music selected will be limited to pop, folk, rock, metal, jazz and religious music.
TREATMENT OF DATA

Vocal extraction
In order to analyze the language of the lyrics, the vocals will have to be isolated from the rest of the background music. This will be done using frequency filters and lowering the levels in which everything non-vocal will be played and read at.

Sampling
Due to the large database size and amount of data to be compared, the strategy to optimize this will be by using random sampling. Using the microphone or cutting the file, 6 seconds will be taken in and then 15 six second audio samples will be taken from the language database. From each of these, the sample from the test song will be compared and return a percentage of how close it matches that from the database.

PROJECT TIMELINE
For the progress of the project, a projected timeline has been estimated for each goal. These will stand as a mini deadline for each step of the project and a guideline for how the project will grow and proceed.

Oct 7 – 15
Determine which data to use
Oct 16
Gather the data to be used
Oct 8 - 20
Research music interpretation methods
Oct 20 - 31
Create an organized database system
Nov 1 - 15
Be able to send audio through a microphone
Nov 15 - 20
Run tests and finalize the program
Nov 20 - End
Final adjustments and prepare for the presentation
Future
More releases, bug fixes, more features
  Table 1. The projected schedule on how the project will progress.

TOOLS AND RESOURCES
For the creation of this project, many tools and resources were and will be used. Using GitHub to share the project will help grant easy access to the code and data for the project members. As for a vocal extraction comparison, Audacity will be used as a sample to ensure that the program will achieve an accurate vocal extraction/isolation. However, the Audacity sample will not be used for the final results. The primary language used for the program will be Python, though other languages may be used in cases where Python does not provide a suitable solution. Though the data will be stored in a proper database, the initial data will be stored as .wav files for ease of access and storage.

REFERENCES
V. Chandrasekhar, M. Sargin, D. Ross: Automatic Language Identification in Music Videos with Low Level Audio and Visual Features, Google Inc. 
Librosa Development Team: “Vocal Separation,” Librosa Gallery on GitHub, 2016-2017.
