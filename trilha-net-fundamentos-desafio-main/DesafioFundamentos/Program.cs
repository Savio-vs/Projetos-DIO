using DesafioFundamentos.Models;

// Coloca o encoding para UTF8 para exibir acentuação
Console.OutputEncoding = System.Text.Encoding.UTF8;

decimal precoInicial = 0;
decimal precoPorHora = 0;

Console.WriteLine("Seja bem vindo ao sistema de estacionamento!\n" +
                  "Digite o preço inicial de entrada:");
precoInicial = Convert.ToDecimal(Console.ReadLine());

Console.WriteLine("Agora digite o preço por hora:");
precoPorHora = Convert.ToDecimal(Console.ReadLine());

// Instancia a classe Estacionamento, já com os valores obtidos anteriormente
Estacionamento es = new Estacionamento(precoInicial, precoPorHora);

string opcao = string.Empty;
bool exibirMenu = true;

// Realiza o loop do menu
while (exibirMenu)
{
    Console.Clear();
    Console.WriteLine("===========================");
    Console.WriteLine("|| Digite a sua opção:   ||");
    Console.WriteLine("|| 1 - Cadastrar veículo ||");
    Console.WriteLine("|| 2 - Remover veículo   ||");
    Console.WriteLine("|| 3 - Listar veículos   ||");
    Console.WriteLine("|| 4 - Encerrar          ||");
    Console.WriteLine("===========================");

    switch (opcao = Console.ReadLine())
    {
        case "1":
            es.AdicionarVeiculo();
            break;

        case "2":
            es.RemoverVeiculo();
            break;

        case "3":
            es.ListarVeiculos();
            break;

        case "4":
            exibirMenu = false;
            Console.WriteLine("Encerrando Programa...");
            break;

        default:
            Console.Clear();
            Console.WriteLine("Opção inválida\nSó são validas opções entre 1 e 4.");
            break;
    }
    Console.WriteLine("\n=======================================");
    Console.WriteLine("Precione Qualquer tecla para continuar:");
    Console.WriteLine("=======================================");
    Console.ReadLine();
    //await Task.Delay(5000);
}


