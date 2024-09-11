PROMPT = '''You will be provided with a string representation of a PDF form. This form contains several fields, such as name, age, address, etc., which need to be extracted.
Analyze the structure of the provided string to identify and differentiate each field.
Create regex patterns for each field (e.g., Name, Age, Address, etc.) that can be applied to future forms of the same format to extract the relevant information accurately.
Generate your response in a json format where each field is the key and then regex is a string as data.
Your output should be in this format (example):
{
Name: *regex*
Age: *regex*
...
}
Do not add anything else in your response, so that this may be instantly used without modification
'''


