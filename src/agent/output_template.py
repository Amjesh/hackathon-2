

def output_template(templateOutput):
    # HTML table template
    html_table = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="tableStyles.css">
            <title>HTML Table with External CSS</title>
            <style>
                /* Additional styles for the pop-up */
                .popup {
                    display: none;
                    width:50%;
                    position: fixed;
                    top: 30%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    padding: 20px;
                    background-color: #fff;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
                    z-index: 1;
                }

                /* Styling for the button */
                #popupButton {
                    background-color: black;
                    color: white;
                    padding: 10px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                }
            </style>
        </head>
        <body>
            <div class="table-container">
                <table>
                    <tr>
                        <th>Rank</th>
                        <th>Name</th>
                        <th>CV link</th>
                        <th>Experience</th>
                        <th>Education</th>
                        <th>Highlights</th>
                        <th>Don't Meet Criteria</th>
                        <th>Score</th>
                    </tr>
    """

    # Add the button to the first row with rowspan=4
    html_table += '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>\n'.format(
        templateOutput[0]["Rank"], templateOutput[0]["Name"], templateOutput[0]["CV link"], templateOutput[0]["Experience"],
        templateOutput[0]["Education"], templateOutput[0]["Highlights"], templateOutput[0]["Don't Meet Criteria"],
        templateOutput[0]["Score"]
    )

    # Add the remaining rows
    for entry in templateOutput[1:]:
        # Use format() to avoid backslash issues
        html_table += '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>\n'.format(
            entry["Rank"], entry["Name"], entry["CV link"], entry["Experience"], entry["Education"], entry["Highlights"],
            entry["Don't Meet Criteria"], entry["Score"]
        )

    html_table += """
                </table>
            </div>

            <!-- Pop-up container -->
            <div id="popup" class="popup">
                <p id="popupText"></p>
                <button onclick="closePopup()">Close</button>
            </div>

            <!-- JavaScript functions for the pop-up -->
            <script>
                function openPopup(text) {
                    document.getElementById('popupText').innerText = text;
                    document.getElementById('popup').style.display = 'block';
                }

                function closePopup() {
                    document.getElementById('popup').style.display = 'none';
                }
            </script>
        </body>
        </html>
    """
    return html_table
