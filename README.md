# render_function_graphs

<b>The work is going on our gui version. You can check it on "wxPython_gui" branch</b>


Program for render function graphics by equation of function graph. You can always help with code or ideas to improve usability of this script.

If you want to check out GUI versions change master branch to add_gui (Tkinter) or wxPython_gui (wxPython)

=====================================================

This program uses matplotlib and numpy lib for rendering function graphs, so without this libs script won't work.

You have to enter f(x) function to get the function graph. An input is in infinity loop, so you can get new function graph just by closing the window of the old graph and entering new function. You can end the execution of the program by entering 'q'.

- You have to use double stars to raise a number to the power of n, <code>x**2</code> instead of <code>x^2</code>;
- You have to use vertical slashes to get absolute statement. It can be like <code>|2*x|</code>;
- You always have to use stars to multiply values, <code>2*x</code> instead of <code>2x</code>;
- Use trigonometrical functions like this <code>sin, cos, tan and etc</code>;
- Use <code>{</code> symbol to render system of equation graphs. Example: <code>{5/x, x<=-1; -x**2+4*x, x>-1</code>, where <code>;</code> is using to separate equations and <code>,</code> to define the range of **x** values.
