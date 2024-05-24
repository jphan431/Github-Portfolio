import java.io.File; 
import java.io.IOException; 
import java.util.Scanner; 
  
import javax.sound.sampled.AudioInputStream; 
import javax.sound.sampled.AudioSystem; 
import javax.sound.sampled.Clip; 
import javax.sound.sampled.LineUnavailableException; 
import javax.sound.sampled.UnsupportedAudioFileException;
import javax.sound.sampled.AudioFormat;
import javax.sound.sampled.SourceDataLine;
import javax.sound.sampled.DataLine.Info;

import static javax.sound.sampled.AudioSystem.getAudioInputStream;
import static javax.sound.sampled.AudioFormat.Encoding.PCM_SIGNED;

/*
    To compile: javac SpotifyLikeApp.java
    To run: java SpotifyLikeApp
 */

// declares a class for the app
public class SpotifyLikeApp {

    // global variables for the app
    String status;
    Long position;
    static Clip audioClip;

    // "main" makes this class a java app that can be executed
    public static void main(final String[] args) {

        // create a scanner for user input
        Scanner input = new Scanner(System.in);

        String userInput = "";
        while (!userInput.equals("q")) {

            menu();

            // get input
            userInput = input.nextLine();

            // accept upper or lower case commands
            userInput.toLowerCase();

            // do something
            handleMenu(userInput);

        }

        // close the scanner
        input.close();

    }


    /*
     * displays the menu for the app
     */
    public static void menu() {

        System.out.println("---- SpotifyLikeApp ----");
        System.out.println("[H]ome");
        System.out.println("[S]earch by title");
        System.out.println("[L]ibrary");
        System.out.println("[P]lay");
        System.out.println("[Q]uit");

        System.out.println("");
        System.out.print("Enter q to Quit:");

    }

    /*
     * handles the user input for the app
     */
    public static void handleMenu(String userInput) {

        switch(userInput) {

            case "h":
                System.out.println("-->Home<--");
                break;

            case "s":
                System.out.println("-->Search by title<--");
                search();
                break;

            case "l":
                
                displayLibrary();
                search();
                break;
                
                
            case "p":
                System.out.println("-->Play<--");
                play(filepath[0]);
                break;

            case "q":
                System.out.println("-->Quit<--");
                break;

            default:
                break;
        }

    }
// Array for songs

private static void displayLibrary(){
    System.out.println("-->Library<--");
    for(int i  = 0; i< 10; i++){
       
        
    System.out.println(title[i]);
    System.out.println(artist[i]);
    System.out.println(year[i]);
    System.out.println(genre[i]);
    System.out.println(filepath[i]);
    {
   
    
    
  
    }
}
    }

    



private static void search()



{
    System.out.print("Enter a song to search: ");

    Scanner input = new Scanner(System.in);
    String userInput = "";
    userInput = input.nextLine();
  
    for(int n = 0; n<10; n++){
        if(title[n].equals(userInput))

        {
            System.out.println(title[n]);
            System.out.println(filepath[n]);
            System.out.println(artist[n]);
            System.out.println(year[n]);
            System.out.println(genre[n]);
            play(filepath[n]);

        }
        

        
        
        
    }

    //Read song input title
    //For loop to search the title
    //if match found, play
    //not display message
}



// try to create an array for each field in music file
// a field is title artist year genre file path
// there should be an array for each field under this reduced design

 
//String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
static String[] title = {"Cement Lunch", "Journey of King", "Tanzen", "Wirklich_Wichtig","Vacaciones_salsa", "El Preso Numero Nueve", "Welcome", "Burn It Down", "Storybook", "Zumbido"};
static String[] artist = {"Ava Luna", "Bisou", "Checkie Brown", "Checkie Brown", "Dee Yan-Key", "Kathleen_Martin", "Kitkat Club", "Mid-Air Machine", "Scott Holmes", "The Dubbystyle" };
static String[] year =  {"2010", "2019", "2019", "2019", "2018", "2016", "2018", "2017", "2020", "2019"  };
static String[] genre = {"Funk", "Electronic", "Jazz", "Jazz", "Folk", "Blues", "Instrumental", "Jazz", "Country", "Dub"};
static String[] filepath = {"Ava_Luna_-_02_-_Cement_Lunch.wav", "Bisou_-_04_-_Journey_of_King.wav", "Checkie_Brown_-_10_-_Tanzen_CB_003.wav", "Checkie_Brown_-_11_-_Wirklich_Wichtig_CB_27.wav", "Dee_Yan-Key_-_10_-_vacaciones_salsa.wav", "Kathleen_Martin_-_02_-_El_Preso_Numero_Nueve.wav", "Kitkat_Club_-_02_-_Welcome.wav", "Mid-Air_Machine_-_Burn_It_Down.wav", "Scott_Holmes_-_Storybook.wav", "The_Dubbstyle_-_05_-_Zumbido.wav" };



// "title": "Cement Lunch" ,
// "artist" : "Ava Luna" ,
// "year" : "2010" ,
// "genre": "Funk" ,
// "filepath": "Ava_Luna_-_02_-_Cement_Lunch.wav"

// "title": "Journey of King" ,
// "artist": "Bisou" ,
// "year": "2019"
// "genre": "Electronic" ,
// "filepath": "Bisou_-_04_-_Journey_of_King.wav"

// "title": "Tanzen" ,
// "artist": "Checkie Brown" ,
// "year": "2019" ,
// "genre": "Jazz" ,
// "filepath": "Checkie_Brown_-_10_-_Tanzen_CB_003.wav"

// "title": "Wirklich_Wichtig" ,
// "artist": "Checkie Brown" ,
// "year": "2019"
// "genre": "Jazz" ,
// "filepath": "Checkie_Brown_-_11_-_Wirklich_Wichtig_CB_27.wav"


// "title": "Vacaciones_salsa" ,
// "artist": "Dee Yan-Key" ,
// "year": "2018" ,
// "genre": "Folk" ,
// "filepath": "Dee_Yan-Key_-_10_-_vacaciones_salsa.wav"

// "title": "El Preso Numero Nueve" ,
// "artist": "Kathleen_Martin" ,
// "year": "2016" ,
// "genre": "Blues" ,
// "filepath":  "Kathleen_Martin_-_02_-_El_Preso_Numero_Nueve.wav"

// "title": "Welcome" ,
// "artist": "Kitkat Club" ,
// "year": "2018" ,
// "genre": "Instrumental"
// "filepath": "Kitkat_Club_-_02_-_Welcome.wav"

// "title": "Burn It Down" ,
// "artist": "Mid-Air Machine" ,
// "year": "2017" ,
// "genre": "Jazz" ,
// "filepath": "Mid-Air_Machine_-_Burn_It_Down.wav"

// "title": "Storybook" ,
// "artist": "Scott Holmes" ,
// "year": "2020" ,
// "genre": "Country" ,
// "filepath": "Scott_Holmes_-_Storybook.wav"

// "title": "Zumbido" ,
// "artist": "The Dubbystyle" ,
// "year": "2019" ,
// "genre": "Dub" ,
// "filepath": "The_Dubbstyle_-_05_-_Zumbido.wav"




  


    /*
     * plays an audio file
     */
    public static void play(String song) {

        // open the audio file
        final File file = new File(song);
       

        try {
        
            // create clip 
            audioClip = AudioSystem.getClip();

            // get input stream
            final AudioInputStream in = getAudioInputStream(file);

            audioClip.open(in);
            audioClip.setMicrosecondPosition(0);
            audioClip.loop(Clip.LOOP_CONTINUOUSLY);

        } catch(Exception e) {
            e.printStackTrace(); 
        }

    }


}

