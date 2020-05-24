class Reptil {
    constructor(nome, cor, idade) {
      this.nome = nome;
      this.cor = cor;
      this.idade = idade;
    }
    tomar_sol() {
        return `${this.nome} Tomando sol`
    }

  }

  const reptil = new Reptil("joao", "azul", 10)

  console.log(reptil.tomar_sol())