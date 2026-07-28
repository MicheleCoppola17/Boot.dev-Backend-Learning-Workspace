/*
Assignment
Complete the snek_score function in exercise.c. 
Sneklang is unique™ in that its toolchain gives developers a "project score" that's dependent on how maintainable and "high quality" their codebase is. The larger the score, the harder it is to work in the project. The score is calculated as follows:

1. Multiply the number of files by the number of commits to get the size factor
2. Add the size factor to the number of contributors to get the complexity factor
3. Multiply the complexity factor by the average bug criticality (a number between 0 and 1) to get the final score
*/

float snek_score(int num_files, int num_contributors, int num_commits, float avg_bug_criticality) {
    int project_size = num_files * num_commits;
    int project_complexity = project_size + num_contributors;
    return (float)project_complexity * avg_bug_criticality;
}
