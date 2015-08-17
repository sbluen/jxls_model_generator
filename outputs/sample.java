public class Sample {
    public Sample(String a, String b, String cd, String e_f) {
        this.a = a;
        this.b = b;
        this.cd = cd;
        this.e_f = e_f;
    }
    
    public Sample(ArrayList source) {
        this.a = source.get(a);
        this.b = source.get(b);
        this.cd = source.get(cd);
        this.e_f = source.get(e_f);
    }
    
        public void setA(String a) {
        this.a = a;
    }
    
        public void setB(String b) {
        this.b = b;
    }
    
        public void setCd(String cd) {
        this.cd = cd;
    }
    
        public void setE_f(String e_f) {
        this.e_f = e_f;
    }
    
    
        public String getA() {
        return a;
    }
    
        public String getB() {
        return b;
    }
    
        public String getCd() {
        return cd;
    }
    
        public String getE_f() {
        return e_f;
    }
    
    
}
