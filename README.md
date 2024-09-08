# IDLE Enhancement Suite: Highlighting and Navigation Tools

## Course Context
This project was developed as part of the **Working with Large Code Bases** course at UC San Diego. The course focuses on equipping students with the skills necessary to effectively navigate, understand, and contribute to large codebases, a crucial competency for software engineers in the industry. Through this project, we applied these principles by enhancing the IDLE code editor with advanced highlighting and navigation features.

## Team Members
- **Chenfei Yan**  
- **Jacky Hu**  
- **Chengcheng Zhang**  

## Project Summary
Our project, developed in **Python**, introduces a line marking feature to the IDLE code editor, enabling users to highlight specific lines or regions of code in various colors. This enhancement improves code readability and navigation, especially in large codebases. Highlights are persistent across sessions, as the information is stored in a JSON file. Additionally, users can easily navigate through highlighted sections using the "Find Next Highlight" feature.

## Progress Report
We have successfully implemented the core functionality and are currently refining the user interface and adding advanced features. Below is a summary of our progress:

### Completed Tasks
- **Highlighting Functionality**: Implemented the ability to highlight text in one and multiple colors.
- **User Interface**: Added buttons and a drop-down menu for selecting highlight colors.
- **Persistence**: Integrated JSON storage to ensure highlights persist across sessions.
- **Bug Fixes**: Resolved issues related to color changes affecting other highlighted regions and ensured proper selection display.
- **Unit Testing**: Developed unit tests to validate the functionality.

## Challenges and Solutions

### 1. Tag Name Issue
We encountered a problem where changing the highlight color of one region inadvertently affected other regions with the same tag. We resolved this by reassigning tags based on the new color, ensuring that only the intended region's color was modified.

### 2. Selection Color Issue
The typical grey selection color was not appearing when text was highlighted. We addressed this by adjusting the selection priority using `tag_raise("sel")`, ensuring the selection color displayed correctly.

### 3. Dropdown Menu Parameters
We faced challenges in passing color parameters to the `toggle_highlight` function due to the limitations of `tkinter`. By using lambda functions, we successfully passed the color parameters, allowing users to choose different colors from the dropdown menu.

### 4. Redundant Tags for Unhighlighting
An issue arose when unhighlighting a region, as it created a redundant tag associated with the "white" color. We implemented a check to remove these tags, preventing them from interfering with other functionality.

## Project Functionality
The project allows users to highlight selected text regions in various colors such as blue, red, yellow, green, orange, and purple. Users can revert any highlighted region to its original color and navigate through highlighted sections using the "Find Next Highlight" and "Find First Highlight" buttons.

![Highlighting Example](https://github.com/cse190largecodebases/group-project-idlemasters/assets/77074167/ec2631f6-f541-4466-a80d-00b06a8a10b4)

## User Interface
The user interface includes a drop-down menu for color selection, with unclickable buttons when no file is open. Highlight colors are designed to ensure readability.

![User Interface Example](https://github.com/cse190largecodebases/group-project-idlemasters/assets/77074167/3e0dedbf-fc1a-4fd3-99c1-58c38fe59ca5)
![Color Selection Example](https://github.com/cse190largecodebases/group-project-idlemasters/assets/77074167/20a58eb8-d490-4a69-8cfa-fa7314fb3a3e)

## Implementation Overview
Our initial step was to implement a basic highlighting feature in a single color (blue). We then extended this to support multiple colors, each linked to a drop-down menu. The highlight information is stored in JSON format, allowing it to persist across sessions. The "Find Next Highlight" feature was implemented by sorting and navigating through the highlighted regions.

![Implementation Overview](https://github.com/cse190largecodebases/group-project-idlemasters/assets/114633485/6681a534-5e1a-4d88-bb1d-909193fa8db3)

## Testing
We have developed comprehensive unit tests to validate each function in our project:

- **test_toggle_highlight**: Validates the basic highlighting functionality.
- **test_highlight_save**: Ensures highlight information is correctly saved to a JSON file.
- **test_highlight_reopen**: Confirms that highlights are correctly reloaded from the JSON file.
- **test_next_wrap**: Tests the "Find Next Highlight" feature, ensuring it wraps around when reaching the end of the text.
- **test_next_normal**: Verifies that the "Find Next Highlight" function navigates correctly through the text based on the order of highlights.

## Running the Project
To run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/MerlinZCC/IDLE-Enhancement-Suite-Highlighting-and-Navigation-Tools.git
   ```
   
2. **Navigate to the Project Directory**:
   ```bash
   cd IDLE-Enhancement-Suite-Highlighting-and-Navigation-Tools
   ```

3. **Run IDLE with the Enhanced Features**:
   - Open IDLE from within this directory, ensuring the Python environment recognizes the modifications.
   - Use the enhanced highlighting and navigation tools directly within the IDLE editor.

## Conclusion
This Python project, developed as part of the **Working with Large Code Bases** course, enhances the IDLE code editor by introducing a robust line marking feature. It provides users with a more efficient way to navigate and manage large codebases, which is crucial for software engineering roles in industry. Through careful design, testing, and implementation, we have created a tool that significantly improves the user experience in IDLE.
