using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using janela.Models;

namespace janela.Controllers;

public class LuvasController : Controller
{
    private readonly ILogger<LuvasController> _logger;

    public LuvasController(ILogger<LuvasController> logger)
    {
        _logger = logger;
    }

    public IActionResult Index()
    {
        return View();
    }

    [HttpPost]
    public IActionResult Signin(UsersModel model)
    {
        return View("ViewUsers", model);
    }

    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
}
