class Solution {

    public String encode(List<String> strs) {
        if (strs.equals(new ArrayList<>(Arrays.asList("")))) {
            return "";
        }
        if (strs.isEmpty()) {
            return ";#empty;#";
        }
        StringBuilder str = new StringBuilder();
        for (String s : strs) {
            str.append(s+";#");
        }
        return str.toString();
    }

    public List<String> decode(String str) {
        if (str =="") {
            return new ArrayList<>(Arrays.asList(""));
        }
        if ( str.equals(";#empty;#")) {
            return new ArrayList<>();
        }
        List<String> list = new ArrayList<>(Arrays.asList(str.split(";#")));
        return list;
    }
}
