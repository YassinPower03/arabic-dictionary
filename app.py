import os
import logging
from flask import Flask, render_template, request, jsonify, redirect, url_for
from dictionary_data import arabic_dictionary, get_word_info

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create Flask application
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")

@app.route('/')
def index():
    """Render the main page of the dictionary application."""
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    """Handle word search functionality."""
    if request.method == 'POST':
        word = request.form.get('word', '').strip()
        return redirect(url_for('word_details', word=word))
    
    word = request.args.get('word', '').strip()
    if word:
        return redirect(url_for('word_details', word=word))
    return redirect(url_for('index'))

@app.route('/word/<word>')
def word_details(word):
    """Display detailed information about a specific word."""
    word_info = get_word_info(word)
    
    # Dictionary of language names for translation display
    lang_names = {
        'english': 'الإنجليزية',
        'french': 'الفرنسية',
        'spanish': 'الإسبانية'
    }
    
    if word_info:
        return render_template('word_details.html', word=word, info=word_info, lang_names=lang_names)
    else:
        return render_template('word_details.html', word=word, info=None, not_found=True, lang_names=lang_names)

@app.route('/api/search', methods=['GET'])
def api_search():
    """API endpoint for searching words."""
    query = request.args.get('q', '').strip()
    suggestions = []
    
    if query:
        # Find words that start with the query (maximum 10 suggestions)
        suggestions = [word for word in arabic_dictionary.keys() 
                      if word.startswith(query)][:10]
    
    return jsonify(suggestions)

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('index.html', error="الصفحة غير موجودة"), 404

@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors."""
    return render_template('index.html', error="حدث خطأ في الخادم"), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
