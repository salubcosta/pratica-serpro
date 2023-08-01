package main.java.com.classes;

class Cliente {
    private double renda;
    private char sexo;
    private int anoNascimento;

    public double getRenda(){
        return this.renda;
    }
    public void setRenda(double renda){
        this.renda = renda;
    }

    public char getSexo(){
        return this.sexo;
    }
    public void setSexo(char sexo){
        this.sexo = sexo;
    }

    public int getAnoNascimento(){
        return this.anoNascimento;
    }
    public void setAnoNascimento(int anoNascimento){
        this.anoNascimento = anoNascimento;
    }
}