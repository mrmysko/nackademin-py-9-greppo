            """if invert_match:
                for index, line in enumerate(reader):

                    # Reset search_word tracker.
                    search_word_dict = dict((i, 0) for i in search_terms)

                    if show_line_numbers:
                        for key in search_word_dict.keys():
                            # Returns a match object. True if a match is found.
                            if re.search(rf"\b{key}\b", line):
                                search_word_dict[key] = True

                        # Returns False if any value in search_word_dict is True.
                        if not any(search_word_dict.values()) and len(line) > 1:
                            match_lines.append(rf"{file}:{index}:{line.strip()}")"""
                        """Now, hur kokar jag ner den här i en list comprehension?"""

                    """else:
                        for key in search_word_dict.keys():
                            if re.search(rf"\b{key}\b", line):
                                search_word_dict[key] = True

                        if not any(search_word_dict.values()) and len(line) > 1:
                            match_lines.append(rf"{file}:{line.strip()}")

            if show_line_numbers:
                match_lines.extend(
                    [
                        f"{file}:{index}:{line.strip('\n')}"
                        for x in search_terms
                        for index, line in enumerate(reader)
                        if re.search(rf"\b{x}\b", line)
                    ]
                )
            else:
                match_lines.extend(
                    [
                        f"{file}:{line.strip('\n')}"
                        for x in search_terms
                        for line in reader
                        if re.search(rf"\b{x}\b", line)
                    ]
                )""""""

                # print(search_word_dict)