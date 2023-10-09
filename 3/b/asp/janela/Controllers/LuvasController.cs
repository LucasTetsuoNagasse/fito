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
    [HttpGet]
    public IActionResult Signin()
    {
        return View();
    }
    [HttpPost, ActionName("SignIn")]
    public IActionResult SigninP(UsersModel model)
    {
        return RedirectToAction("ViewUsers", model);
    }
    public IActionResult ViewUsers()
    {
        return View();
    }

    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
}
