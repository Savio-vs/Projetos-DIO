using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace DesafioFundamentos.Models.tipoAutomovel
{
    public class Automovel
    {
        private decimal valorInicial = 0;
        
        public string placa,tipoVeiculo;
        public Automovel(decimal valorInicial, string placa, string tipo){
            this.valorInicial = valorInicial;
            this.placa = placa;
            this.tipoVeiculo = tipo;
        }
        
        public decimal getValor(){
            return this.valorInicial;
        }
        
    }   
    
}