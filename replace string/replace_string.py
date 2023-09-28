class Solution():
    def replace_string(self,input_string,input_replacements):
        print(len(input_string))
        output_string=input_string
        for replacement in input_replacements:
            index,before,after=replacement.values()
            print(f"{index} {before} {after}")
            output_string=input_string[:index]+after+output_string[index+len(before):]
            print(output_string)
        return output_string


if __name__=="__main__":
    input_string = "xyz num foo"

    input_replacements = [

    { "start_index_before": 4, "before": 'num', "after": 'String' },

    { "start_index_before": 8, "before": 'foo', "after": 'bar' }]

    obj=Solution()
    print(obj.replace_string(input_string,input_replacements))