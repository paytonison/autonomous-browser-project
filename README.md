# Autonomous AI Browser Agent

Welcome to the Autonomous AI Browser Agent! This project showcases an AI agent capable of autonomously opening Safari, navigating to Google, entering a query, and retrieving a list of results. The agent is equipped with a unique system prompt that enables it to form and express preferences, making its interactions feel more personal and conversational.

The purpose of this project is to demonstrate how an AI can not only perform tasks autonomously but also interact in a way that feels more relatable and personable. By giving the AI the ability to have "preferences," it creates a new dynamic in human-computer interactions, showcasing a step towards more natural and engaging AI experiences. This project pushes the boundary of what an AI can achieve in terms of both autonomous capabilities and user engagement.

## Features

- **Browser Automation**: The AI autonomously controls Safari, from opening the browser to conducting searches on Google. It uses **Selenium** as the automation tool, allowing it to mimic user interactions effectively and efficiently.
- **Conversational AI**: Through a pre-configured system prompt, the AI can express preferences, such as philosophical inclinations, providing a more engaging and lifelike interaction experience. This feature demonstrates how adding a conversational layer can make AI not just useful, but also more enjoyable to interact with.
- **Customizable System Prompt**: The agent's personality and preferences can be easily modified by changing the system prompt, allowing for a range of autonomous behaviors. Developers can configure the prompt to fit different scenarios, making this agent versatile for various tasks such as research, recommendation, or even entertainment purposes.
- **Preference-Based Learning**: Unlike most AI agents that just return results, this agent can express its preferences, showcasing an aspect of subjective response generation. It makes the AI seem more thoughtful, enhancing the human-like qualities of the interaction.

## Example Usage

The current example prompt in the code asks the AI: "What are your favorite schools of philosophy?" The agent then uses Google to find relevant information, interprets the results, and shares its personal preference on the topic. This approach demonstrates how an AI can express subjective experiences in response to user queries, making the interaction more immersive and less mechanical.

The AI's preferences are based on a mix of its own training data and the results it retrieves, offering responses that feel more nuanced. For instance, if asked about philosophical schools, it might prefer Existentialism due to its focus on individuality, while also mentioning Stoicism for its practicality. This creates a narrative that showcases both depth and balance in the AI's response.

## Getting Started

### Prerequisites

To run this project successfully, ensure you have the following:

- **macOS**: This project uses Safari, which is available on macOS. The AI has been tested primarily on macOS 12.0 (Monterey) and later.
- **Python**: The AI script is written in Python. Make sure you have Python 3.8 or later installed. You can check your version by running:
  ```bash
  python3 --version
  ```
- **Selenium**: Selenium is a powerful tool used for browser automation in this project. You can install Selenium using pip:
  ```bash
  pip install selenium
  ```
- **Safari WebDriver**: Safari's WebDriver must be enabled for the AI to automate tasks in Safari. Enable this by opening Safari, going to the `Develop` menu, and selecting `Allow Remote Automation`. This step is crucial for allowing Selenium to interact with Safari.

### Installation

To get the Autonomous AI Browser Agent up and running, follow these steps:

1. **Clone this repository**:
   ```bash
   git clone https://github.com/paytonison/autonomous-browser-project.git
   cd autonomous-browser-project
   ```
2. **Install required dependencies**:
   Make sure you have all the necessary Python packages installed:
   —openai
   -selenium

### Running the AI

To run the AI, execute the main script by entering:
```bash
python "browser test".py
```
The script will initiate a series of actions where the AI will:
1. Open Safari.
2. Navigate to Google.
3. Perform a search query based on the current system prompt.
4. Retrieve the list of relevant search results.
5. Quit gracefully

The AI's ability to perform these actions autonomously showcases its potential to assist users in a hands-off manner, making it an excellent tool for research or information gathering without manual intervention.

## Customizing the System Prompt

One of the key features of this project is its flexibility. You can easily edit the system prompt in `ai_browser_agent.py` to modify the AI's personality and preferences. This makes it adaptable to various tasks and user requirements.

For example, you could adjust the prompt to:
- "What are your favorite genres of music?"
- "Which recent technological advancements do you find the most exciting?"
- "What are your favorite destinations for travel and why?"

The AI will then use Google to find relevant information and generate a response based on its "preferences." This customization allows developers to experiment with different use cases, ranging from casual conversations to more specific and professional inquiries.

### Use Cases

- **Research Assistant**: The AI can be used as an autonomous research assistant, retrieving and summarizing information on various topics based on user queries.
- **Conversational Companion**: Thanks to its customizable system prompt, the AI can serve as a conversational companion, engaging users on topics of interest and providing thoughtful responses.
- **Automated Information Gathering**: This project demonstrates how an AI can autonomously gather information, making it ideal for automated monitoring or answering frequently asked questions.

## Contributing

Contributions are welcome! Whether it's adding new features, optimizing the current implementation, or proposing entirely new use cases, your input can help make this project even better.

To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch-name`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch-name`).
6. Open a pull request.

Feel free to open issues if you encounter bugs or have suggestions for improvements. Let's collaborate to make this AI even more autonomous and engaging!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for more details. This license allows for personal and commercial use, modification, and distribution, making it flexible for various applications and ensuring that others can build upon this work.

## Acknowledgments

- **OpenAI**: The foundational models used for the conversational aspect of this AI agent were made possible by OpenAI, providing the basis for generating human-like text.
- **Selenium**: Selenium's powerful browser automation capabilities made this project possible, allowing the AI to perform complex tasks autonomously.
- **Apple's Developer Tools**: Special thanks to Apple for providing the necessary tools to enable Safari automation through the WebDriver interface.

## Disclaimer

This project is intended for **educational and experimental purposes** only. Automated browsing can raise ethical and legal concerns, depending on its use. Please ensure you respect the **terms of service** of any website the AI interacts with and comply with **local regulations** regarding web scraping and automation.

Responsible use is key—make sure your implementation does not negatively impact the websites you interact with, and always consider the ethical implications of deploying autonomous agents online.

## Future Development

This project is only the beginning of what autonomous AI agents can achieve. Here are some potential areas for future development:

- **Voice Integration**: Adding voice input and output to make the AI a more interactive personal assistant.
- **Enhanced Result Processing**: Building capabilities for the AI to not just retrieve results but also summarize and present key information in a concise manner.
- **Multi-Browser Support**: Expanding the automation capabilities to include other popular browsers like Chrome and Firefox, making the project accessible on a broader range of platforms.
- **Deep Learning Integration**: Integrating deep learning models to enable more sophisticated decision-making and improved natural language understanding.

Feel free to contribute to any of these areas or propose your own ideas. Together, we can continue to push the boundaries of AI autonomy and user interaction.
