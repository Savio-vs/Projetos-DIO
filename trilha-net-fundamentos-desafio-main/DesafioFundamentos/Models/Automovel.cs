using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace DesafioFundamentos.Models.tipoAutomovel
{
    public class Automovel
    {
        private decimal valorInial = 0;
        
        public string placa,tipoVeiculo;
        public Automovel(decimal valorInial, string placa, string tipo){
            this.valorInial = valorInial;
            this.placa = placa;
            this.tipoVeiculo = tipo;
        }
        
        public decimal getValor(){
            return this.valorInial;
        }
        
    }   
    
}