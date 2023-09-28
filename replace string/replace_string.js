let input_string = "xyz num foo"

let input_replacements = [

    { start_index_before: 4, before: 'num', after: 'String' },

    { start_index_before: 8, before: 'foo', after: 'bar' }];

// function replace_string(input_string,input_replacements){
//     var output_string=input_string
//     input_replacements.forEach(replace => {
//         var index=replace.start_index_before
//         let before_word=replace.before
//         let count=0
//         for(let i=0;i<replace.before.length;i++){
//             if(input_string[index+i]==before_word[i]){
//                 count+=1
//             }
//             else{
//                 throw("Word Not Found at index")
//             }
//             if(count==replace.before.length-1){
//                 let shift=replace.after.length-replace.before.length
                
//                 for(let i=index;i<output_string.length;i++){
//                     output_string[index+shift]=output_string[index]
//                 }
//                 for(let i=0;i<replace.after.length;i++){
//                     output_string[index]=replace.after[i]
//                 }
//             }
            
//         }    
//     });
//     return output_string
// }


// output_string = "xyz String bar"


function replaceWords(input_string, input_replacements) {
    let output_string = input_string;

    input_replacements.forEach(replace => {
        const { start_index_before, before, after } = replace;
        const index = start_index_before;

        if (output_string.indexOf(before, index) === index) {
            output_string =
                output_string.slice(0, index) +
                after +
                output_string.slice(index + before.length);
        }
    });

    return output_string;
}

console.log(replaceWords(input_string,input_replacements))

