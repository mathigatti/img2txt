# Image to Text conversion utilities

You can find here a small tokenization framework and examples of table extraction from images using Google Vision API. Google provides a good OCR to extract text from images but the output is not the best sometimes in this repository I provide a simple postprocessing of the output in order to make it easier to use the API output.

## Demo

### Sample Input
![IMAGE ALT TEXT HERE](https://github.com/mathigatti/img2txt/blob/master/sample/input/sample.png?raw=true)

### Sample Output
```
                          HR Information                                 Contact
                                Position                                  Salary                                  Office                                   Extn.
                              Accountant                                $162,700                                   Tokyo                                    5407
           Chief Executive Officer (CEO)                              $1,200,000                                  London                                    5797
                 Junior Technical Author                                 $86,000                           San Francisco                                    1562
                       Software Engineer                                $132,000                                  London                                    2558
                       Software Engineer                                $206,850                           San Francisco                                    1314
                  Integration Specialist                                $372,000                                New York                                    4804
                       Software Engineer                                $163,500                                  London                                    6222
                       Pre-Sales Support                                $106,450                                New York                                    8330
                         Sales Assistant                                $145,600                                New York                                    3990
             Senior Javascript Developer                                $433,060                               Edinburgh                                    6224
```




## Requirements
- python 3
- python libraries (Try something like: `pip install google-cloud-vision`)
  - google.cloud.vision
  - google.protobuf
  - google.oauth2

## Usage
On the src folder there is an usage example at `table_example.py`, where the tokenization is used to parse the image of a table.

```
python src/table_example.py sample.png
```
