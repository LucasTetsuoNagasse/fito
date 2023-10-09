using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using geladeira.Models;

namespace geladeira.Controllers;

public class QuestonsController : Controller
{
  private readonly ILogger<QuestonsController> _logger;

  public QuestonsController(ILogger<QuestonsController> logger)
  {
    _logger = logger;
  }

  public IActionResult Index()
  {
    return View();
  }
  
  [HttpPost]
  public IActionResult Correct(QuestonsModel model)
  {
    return View(model);
  }

  [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
  public IActionResult Error()
  {
    return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
  }
}
