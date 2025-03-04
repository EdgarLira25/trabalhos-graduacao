package testesjunit;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import control.*;
import org.junit.Before;
import org.junit.Test;
import org.junit.validator.PublicClassValidator;

import elements.*;
public class PacmanTestes {
    public static GameScreen gamePacMan;
    Pacman pac = new Pacman("pacman.png");



    @Test
    public void testlife(){
    assertEquals(1, pac.getLifes());
    pac.addLife();
    pac.addLife();
    assertEquals(3, pac.getLifes());
    pac.rmvlife();
    assertEquals(2, pac.getLifes());
    }


    @Test 
    public void pacmanIsTransposable(){
       assertTrue(pac.isTransposable());

    }

    @Test
    public void pacmanPontos(){
        
        assertEquals(0, pac.getScore());

    }
    
   



}
