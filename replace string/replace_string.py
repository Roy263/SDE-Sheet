class Solution():
    def replace_string(self,input_string,input_replacements):
        output_string=list(input_string)
        offset=0
        for replacement in input_replacements:
            print(output_string)
            index,before,after=replacement.values()
            if(input_string[index:index+len(before)]==before):
                index+=offset
                output_string[index:index+len(before)]=list(after)
                offset+=len(after)-len(before)
        return ''.join(output_string)


if __name__=="__main__":
    input_string = "xyz num foo"

    input_replacements = [

    { "start_index_before": 4, "before": 'num', "after": 'String' },

    { "start_index_before": 8, "before": 'foo', "after": 'bar' }]

    obj=Solution()
    print(obj.replace_string(input_string,input_replacements))