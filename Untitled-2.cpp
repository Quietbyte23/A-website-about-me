#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <limits>

const std::string SCORE_FILE = "highscores.txt";

void printBanner() {
    std::cout << "\n=========================================\n";
    std::cout << "   🎲 NUMBER GUESSING GAME 🎲\n";
    std::cout << "=========================================\n";
}

int readHighScore() {
    std::ifstream inFile(SCORE_FILE);
    int best = 0;
    if (inFile.is_open()) {
        inFile >> best;
        inFile.close();
    }
    return best; // 0 means no score yet
}

void saveHighScore(int score) {
    std::ofstream outFile(SCORE_FILE);
    if (outFile.is_open()) {
        outFile << score;
        outFile.close();
    }
}

int getValidInt(const std::string& prompt, int min, int max) {
    int value;
    while (true) {
        std::cout << prompt;
        if (std::cin >> value && value >= min && value <= max) {
            return value;
        }
        std::cout << "❌ Invalid input. Try again.\n";
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    }
}

int main() {
    std::srand(static_cast<unsigned>(std::time(nullptr)));
    printBanner();

    int highScore = readHighScore();
    if (highScore > 0) {
        std::cout << "🏆 Best score so far: " << highScore << " attempts\n";
    } else {
        std::cout << "🏆 No high score yet — set the first one!\n";
    }

    char playAgain = 'y';
    while (playAgain == 'y' || playAgain == 'Y') {
        int lower = 1, upper = 100;
        int secret = std::rand() % (upper - lower + 1) + lower;
        int attempts = 0;
        int guess = 0;

        std::cout << "\nI picked a number between " << lower << " and " << upper << ".\n";

        while (guess != secret) {
            guess = getValidInt("Your guess: ", lower, upper);
            attempts++;

            if (guess < secret) {
                std::cout << "⬆️  Higher!\n";
            } else if (guess > secret) {
                std::cout << "⬇️  Lower!\n";
            } else {
                std::cout << "\n🎉 Correct! You got it in " << attempts << " attempts.\n";
            }
        }

        // Update high score (lowest attempts wins)
        if (highScore == 0 || attempts < highScore) {
            highScore = attempts;
            saveHighScore(highScore);
            std::cout << "⭐ NEW HIGH SCORE: " << highScore << " attempts!\n";
        } else {
            std::cout << "🏆 High score is still " << highScore << " attempts.\n";
        }

        std::cout << "\nPlay again? (y/n): ";
        std::cin >> playAgain;
    }

    std::cout << "\nThanks for playing! Final best: " << highScore << " attempts.\n";
    return 0;
}