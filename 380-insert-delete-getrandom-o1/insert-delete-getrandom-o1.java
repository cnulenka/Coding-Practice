class RandomizedSet {
    List<Integer> list;
    Map<Integer, Integer> map;
    int currSize = 0;

    public RandomizedSet() {
        list = new ArrayList<>();
        currSize = 0;
        map = new HashMap<>();
    }
    
    public boolean insert(int val) {
        if(map.containsKey(val)){
            return false;
        }
        if(currSize  ==list.size()){
            list.add(val);
            map.put(val, list.size()-1);
        } else {
            list.set(currSize, val);
            map.put(val, currSize);
        }
        currSize++;
        return true;
    }
    
    public boolean remove(int val) {
        if(map.containsKey(val)){
        // get index
        Integer index = map.get(val);
        // put last element at index
        Integer lastElement = list.get(currSize-1);
        list.set(index, lastElement);
        map.put(lastElement,index);
        map.remove(val);
        currSize--;
         return true;
        }
        return false;
    }
    
    public int getRandom() {
    Random rand = new Random();
    int n = rand.nextInt(currSize);
    return list.get(n);
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */