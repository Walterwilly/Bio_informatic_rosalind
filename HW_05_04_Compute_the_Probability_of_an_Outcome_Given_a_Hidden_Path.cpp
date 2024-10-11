#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

// Global variables for probabilities
vector<vector<double>> emission_prob(3, vector<double>(3));  // Emission probabilities for 3 states (A, B, C)
vector<vector<double>> transition_prob(3, vector<double>(3)); // Transition probabilities for 3 states

// Mappers for states and emissions
vector<char> imapper = {'A', 'B', 'C'};
vector<char> emapper = {'x', 'y', 'z'};

// Input emission sequence
string emission_inp = "yyyxxzzyyxxyzyxyzyxzxyxzzzxxzxzzyxyyxzyyxyyxyyyzzxxyyyxyzxzzyyyyxzzyxzyyyxzyxzzzyyxzyxzzzyxxyzxyyxyy";
int N = emission_inp.size();

// Function to map emissions to index
int get_emission_index(char ch) {
    if (ch == 'x') return 0;
    if (ch == 'y') return 1;
    if (ch == 'z') return 2;
    return -1; // Error case
}

// Viterbi algorithm implementation
vector<int> viterbi() {
    // Initialize DP table for storing maximum probabilities
    vector<vector<double>> dp(3, vector<double>(N, 0.0));
    // Table to store back-pointers (for traceback)
    vector<vector<int>> backpointer(3, vector<int>(N, 0));

    // Initialize the first column of the DP table
    for (int state = 0; state < 3; ++state) {
        dp[state][0] = emission_prob[state][get_emission_index(emission_inp[0])];
    }

    // Fill the DP table
    for (int t = 1; t < N; ++t) {
        for (int curr_state = 0; curr_state < 3; ++curr_state) {
            double max_prob = -1;
            int best_prev_state = -1;
            for (int prev_state = 0; prev_state < 3; ++prev_state) {
                // Calculate the probability of transitioning from prev_state to curr_state
                double prob_transition = dp[prev_state][t - 1] * transition_prob[prev_state][curr_state] * emission_prob[curr_state][get_emission_index(emission_inp[t])];
                if (prob_transition > max_prob) {
                    max_prob = prob_transition;
                    best_prev_state = prev_state;
                }
            }
            // Store the best probability and previous state
            dp[curr_state][t] = max_prob;
            backpointer[curr_state][t] = best_prev_state;
        }
    }

    // Traceback to find the most probable state sequence
    int best_final_state = max_element(dp.begin(), dp.end(), [N](const vector<double> &a, const vector<double> &b) { return a[N - 1] < b[N - 1]; }) - dp.begin();
    vector<int> best_path(N);
    best_path[N - 1] = best_final_state;

    // Follow the backpointers to reconstruct the path
    for (int t = N - 1; t > 0; --t) {
        best_final_state = backpointer[best_final_state][t];
        best_path[t - 1] = best_final_state;
    }

    return best_path;
}

int main() {
    // Define emission probabilities for states A, B, and C
    vector<vector<double>> emission_data = {
        {0.15, 0.213, 0.637}, // A: Emission probabilities for x, y, z
        {0.336, 0.171, 0.493}, // B: Emission probabilities for x, y, z
        {0.292, 0.297, 0.411}  // C: Emission probabilities for x, y, z
    };

    // Define transition probabilities for A -> A, B, C, etc.
    vector<vector<double>> transition_data = {
        {0.428, 0.501, 0.071}, // A -> A, B, C
        {0.381, 0.205, 0.414}, // B -> A, B, C
        {0.267, 0.605, 0.129}  // C -> A, B, C
    };

    // Fill the emission probability matrix
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            emission_prob[i][j] = emission_data[i][j];
        }
    }

    // Fill the transition probability matrix
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            transition_prob[i][j] = transition_data[i][j];
        }
    }

    // Run the Viterbi algorithm
    vector<int> result = viterbi();

    // Convert the result (state sequence) into a readable format (A, B, or C)
    string state_sequence = "";
    for (int state : result) {
        state_sequence += imapper[state];
    }

    // Output the most probable state sequence
    cout << "Most probable state sequence: " << state_sequence << endl;

    return 0;
}
