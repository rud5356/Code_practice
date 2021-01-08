import java.util.ArrayList;
import java.util.Arrays;


class Solution {
	public static void main(String[] args) {
		int[] numbers = {2,1,3,4,1};
		solution(numbers);
	}
    public static int[] solution(int[] numbers) {
    	
    	ArrayList<Integer> answers = new ArrayList<Integer>();

        for(int i=0;i<numbers.length;i++) {
        	for(int j=0;j<numbers.length;j++) {
        		if(i==j) {
        			continue;
        		}else {
        			int y = numbers[i]+numbers[j];
            		if(!answers.contains(y)) {
            			answers.add(y);
            		}
        		}
        	}
        }
        int[] answer = new int[answers.size()];
        for(int result=0;result<answers.size();result++) {
        	answer[result]=answers.get(result);
        }
        Arrays.sort(answer);
        	
        
        
        return answer;
    }
}
