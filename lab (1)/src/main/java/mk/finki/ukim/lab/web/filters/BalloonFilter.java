package mk.finki.ukim.lab.web.filters;

import mk.finki.ukim.lab.model.User;

import javax.servlet.*;
import javax.servlet.annotation.WebFilter;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebFilter(filterName = "BalloonFilter")
public class BalloonFilter implements Filter {
    public void destroy() {
    }

    public void doFilter(ServletRequest req, ServletResponse resp, FilterChain chain) throws ServletException, IOException {
        HttpServletRequest request=(HttpServletRequest) req;
        HttpServletResponse response=(HttpServletResponse) resp;
        User user=(User)request.getSession().getAttribute("user");

        String pateka=request.getServletPath();
        if(!pateka.equals("/login") && user==null){
            response.sendRedirect("/login");
        }
        else{
            chain.doFilter(req, resp);
        }
    }

    public void init(FilterConfig config) throws ServletException {

    }

}
