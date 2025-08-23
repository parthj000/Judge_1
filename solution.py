from temp import kapa
import sys,io
import json 


def run_solution_please():
#     test_cases = {
#     "public": [
#         { "input": [[238,3298], [366, 8383]], "expected_output": True },
#         { "input": [2, [111, 222]], "expected_output": False },
#     ],
#     "private": [
#         { "input": [3, [10, 20]], "expected_output": True }
#     ]
# } 
    test_cases = json.loads(sys.argv[1])
    sol = []
    
    for case in test_cases["public"]:
        response = run_each_case(case["input"],case["expected_output"]) 
        if(response[0]=="solved"):
            sol.append(response[1])
    
    for case in test_cases["private"]:
        response = run_each_case(case["input"],case["expected_output"])
        if(response[0]=="solved"):
            sol.append(response[1])
            
    
    print(json.dumps(sol))

    
    
    

def run_each_case(input,expected_out):
    try:
        buffer = io.StringIO()
        sys.stdout = buffer
        correct=0
        out = kapa(*input)
        if(out==expected_out): correct=1
        res={
            "Input":input,
            "Output":out,
            "Expected_out":expected_out,
            "correct":correct,
            "user_prints":buffer.getvalue()
        }
        return ("solved",res) 
    except Exception as e:
        print(e,file=sys.stderr)
        sys.stdout = sys.__stdout__ 
        # directly end the subprocess
        exit(1)
    finally:
        sys.stdout = sys.__stdout__ 
    
        


run_solution_please()




# {
#   public: [
#     { input: '488', expected_output: '899' },
#     { input: [1,[366,8383]], expected_output: true } },
#     { input: [1,[366,8383]], expected_output: true } },

#   ],
#   hidden: [ { input: [1,[366,8383]], expected_output: true } ]
# }
