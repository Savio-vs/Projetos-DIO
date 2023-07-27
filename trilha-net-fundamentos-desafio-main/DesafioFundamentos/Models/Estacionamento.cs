using DesafioFundamentos.Models.tipoAutomovel;

namespace DesafioFundamentos.Models
{
    public class Estacionamento
    {
        private decimal precoInicial = 0;
        private decimal precoPorHora = 0;
        private List<Automovel> veiculos = new List<Automovel>();

        // Construtor da classe
        public Estacionamento(decimal precoInicial, decimal precoPorHora)
        {
            this.precoInicial = precoInicial;
            this.precoPorHora = precoPorHora;
        }

        public void AdicionarVeiculo()
        {   
            /* 
                Pedir ao usuário identificar o tipo de veiculos que estará estacionando,
                caso seja uma moto o valor de entrada é a metado do valor padrão.
            */
            Console.Clear();
            Console.WriteLine("=======================================");
            Console.WriteLine("|| Identificar o tipo de veiculo:    ||");
            Console.WriteLine("|| 1 - Carro:                        ||");
            Console.WriteLine("|| 2 - Moto                          ||");
            Console.WriteLine("=======================================");
            
            try{
                int tipo = Convert.ToInt32(Console.ReadLine());
                // Pedir para o usuário digitar uma placa e adicionar Automovel na lista "veiculos"
                Console.WriteLine("Digite a placa do veículo para estacionar:Padrão(abc-1234).");
                string placa = Console.ReadLine();
                if (tipo == 1)
                {  
                    Automovel c = new Automovel(precoInicial,placa.ToUpper(),"Carro");
                    this.veiculos.Add(c);

                }
                else if(tipo == 2){ 
                    Automovel m = new Automovel(precoInicial/2,placa.ToUpper(),"Moto");
                    this.veiculos.Add(m);
                }
                else{
                    Console.WriteLine("Valor inválido");
                }
            }
            catch(FormatException )
            {
                Console.WriteLine("Formato inválido:\n");
            }
        }

        public void RemoverVeiculo()
        {  
            // Verifica se o veículo existe
            if (veiculos.Count!=0)
            {    
                Console.Clear();
                Console.WriteLine("Digite a placa do veículo para remover:");
                // Pedir para o usuário digitar a placa e armazenar na variável placa
                string placa = Console.ReadLine().ToUpper();
                // Buscar em cada objeto de veiculos a placa correspondente.
                decimal valorTotal=0;
                for(int cont=0;cont<=veiculos.Count;cont++){
                    if (veiculos[cont].placa == placa){

                        Console.WriteLine("Digite a quantidade de horas que o veículo permaneceu estacionado:");
                        int horas = Convert.ToInt32(Console.ReadLine());

                        valorTotal = veiculos[cont].getValor() + this.precoPorHora * horas; 
                        // remover o objeto da lista veiculo tornando o objeto elegivel para coleta de lixo.
                        veiculos.RemoveAt(cont);
                        Console.WriteLine($"O veículo de placa {placa} foi removido e o preço total foi de: R$ {valorTotal}");
                        
                        break;
                    }
                }
                // Verificar se a placa foi encontrada
                if (valorTotal==0){
                    Console.Clear();
                    Console.WriteLine("Desculpe, esse veículo não está estacionado aqui. Confira se digitou a placa corretamente");   
                
                }
            }
            else
            {
                Console.WriteLine("Não existe veiculos cadastrados:");
            }
        }

        public void ListarVeiculos()
        {
            // Verifica se há veículos no estacionamento
            if (veiculos.Any())
            {   
                Console.Clear();
                Console.WriteLine("===================================");
                Console.WriteLine("|| Os veículos estacionados são: ||");
                Console.WriteLine("===================================");
                for(int cont=0;cont<veiculos.Count;cont++){
                    
                    Console.WriteLine($"{veiculos[cont].tipoVeiculo} => {veiculos[cont].placa}");
                }
            }
            else
            {
                Console.WriteLine("Não há veículos estacionados.");
            }
        }
    }
}
