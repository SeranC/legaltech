from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
from datetime import datetime, timedelta
import json
import uuid
import random
import os
from functools import wraps

app = Flask(__name__)
app.secret_key = 'legal_tech_demo_secret_key'

# Product categories as defined in SOW
PRODUCT_CATEGORIES = [
    {"id": "wine", "name": "Wine", "description": "Wine distribution agreements"},
    {"id": "spirit", "name": "Spirit", "description": "Spirit distribution agreements"},
    {"id": "rtd", "name": "Ready-to-Drink", "description": "RTD beverage agreements"},
    {"id": "na", "name": "Non-Alcoholic", "description": "Non-alcoholic beverage agreements"},
    {"id": "beer", "name": "Beer", "description": "Beer distribution agreements"}
]

# User roles with permissions
USER_ROLES = {
    "legal": {
        "name": "Legal",
        "permissions": ["agreement_replication", "create_agreement", "contract_qa", "term_sheet", "financial_analysis", "knowledge_base", "upload"],
        "description": "Full access to all legal tech workflows"
    },
    "finance": {
        "name": "Finance",
        "permissions": ["financial_analysis", "contract_qa", "knowledge_base", "upload"],
        "description": "Financial analysis and contract review access"
    },
    "business": {
        "name": "Business",
        "permissions": ["contract_qa", "knowledge_base", "upload"],
        "description": "Contract Q&A and knowledge base access"
    }
}

# Mock users for demo
MOCK_USERS = [
    {"id": "1", "name": "Sarah Johnson", "email": "sarah.johnson@bbg.com", "role": "legal", "department": "Legal"},
    {"id": "2", "name": "Mike Chen", "email": "mike.chen@bbg.com", "role": "finance", "department": "Finance"},
    {"id": "3", "name": "Jennifer Smith", "email": "jennifer.smith@bbg.com", "role": "business", "department": "Business Development"}
]

# US States for agreement replication
US_STATES = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
]

# Authentication decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def get_current_user():
    if 'user_id' in session:
        return next((user for user in MOCK_USERS if user['id'] == session['user_id']), None)
    return None

def require_product_category(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'product_category' not in session:
            flash('Please select a product category to continue.', 'warning')
            return redirect(url_for('select_category'))
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route('/')
@login_required
def index():
    current_user = get_current_user()
    if 'product_category' not in session:
        return redirect(url_for('select_category'))

    product_category = next((cat for cat in PRODUCT_CATEGORIES if cat['id'] == session['product_category']), None)
    return render_template('dashboard.html',
                         user=current_user,
                         product_category=product_category,
                         user_role=USER_ROLES[current_user['role']],
                         categories=PRODUCT_CATEGORIES)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        user = next((user for user in MOCK_USERS if user['email'] == email), None)

        if user:
            session['user_id'] = user['id']
            flash(f'Welcome back, {user["name"]}!', 'success')
            return redirect(url_for('select_category'))
        else:
            flash('Invalid email address. Please try again.', 'error')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('login'))

@app.route('/select-category', methods=['GET', 'POST'])
@login_required
def select_category():
    current_user = get_current_user()

    if request.method == 'POST':
        category_id = request.form.get('category_id')
        if category_id in [cat['id'] for cat in PRODUCT_CATEGORIES]:
            session['product_category'] = category_id
            flash('Product category selected successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid product category selected.', 'error')

    return render_template('select_category.html',
                         user=current_user,
                         categories=PRODUCT_CATEGORIES,
                         user_role=USER_ROLES[current_user['role']])

# Workflow Routes
@app.route('/agreement-replication')
@login_required
@require_product_category
def agreement_replication():
    current_user = get_current_user()
    if 'agreement_replication' not in USER_ROLES[current_user['role']]['permissions']:
        flash('Access denied. Insufficient permissions.', 'error')
        return redirect(url_for('index'))

    product_category = next((cat for cat in PRODUCT_CATEGORIES if cat['id'] == session['product_category']), None)
    return render_template('agreement_replication.html',
                         user=current_user,
                         product_category=product_category,
                         user_role=USER_ROLES[current_user['role']],
                         states=US_STATES)

@app.route('/create-agreement')
@login_required
@require_product_category
def create_agreement():
    current_user = get_current_user()
    if 'create_agreement' not in USER_ROLES[current_user['role']]['permissions']:
        flash('Access denied. Insufficient permissions.', 'error')
        return redirect(url_for('index'))

    product_category = next((cat for cat in PRODUCT_CATEGORIES if cat['id'] == session['product_category']), None)
    return render_template('create_agreement.html',
                         user=current_user,
                         product_category=product_category,
                         user_role=USER_ROLES[current_user['role']])

@app.route('/contract-qa')
@login_required
@require_product_category
def contract_qa():
    current_user = get_current_user()
    if 'contract_qa' not in USER_ROLES[current_user['role']]['permissions']:
        flash('Access denied. Insufficient permissions.', 'error')
        return redirect(url_for('index'))

    product_category = next((cat for cat in PRODUCT_CATEGORIES if cat['id'] == session['product_category']), None)
    return render_template('contract_qa.html',
                         user=current_user,
                         product_category=product_category,
                         user_role=USER_ROLES[current_user['role']])

@app.route('/term-sheet')
@login_required
@require_product_category
def term_sheet():
    current_user = get_current_user()
    if 'term_sheet' not in USER_ROLES[current_user['role']]['permissions']:
        flash('Access denied. Insufficient permissions.', 'error')
        return redirect(url_for('index'))

    product_category = next((cat for cat in PRODUCT_CATEGORIES if cat['id'] == session['product_category']), None)
    return render_template('term_sheet.html',
                         user=current_user,
                         product_category=product_category,
                         user_role=USER_ROLES[current_user['role']])

@app.route('/financial-analysis')
@login_required
@require_product_category
def financial_analysis():
    current_user = get_current_user()
    if 'financial_analysis' not in USER_ROLES[current_user['role']]['permissions']:
        flash('Access denied. Insufficient permissions.', 'error')
        return redirect(url_for('index'))

    product_category = next((cat for cat in PRODUCT_CATEGORIES if cat['id'] == session['product_category']), None)
    return render_template('financial_analysis.html',
                         user=current_user,
                         product_category=product_category,
                         user_role=USER_ROLES[current_user['role']])

@app.route('/knowledge-base')
@login_required
@require_product_category
def knowledge_base():
    current_user = get_current_user()
    if 'knowledge_base' not in USER_ROLES[current_user['role']]['permissions']:
        flash('Access denied. Insufficient permissions.', 'error')
        return redirect(url_for('index'))

    product_category = next((cat for cat in PRODUCT_CATEGORIES if cat['id'] == session['product_category']), None)
    return render_template('knowledge_base.html',
                         user=current_user,
                         product_category=product_category,
                         user_role=USER_ROLES[current_user['role']])

@app.route('/upload')
@login_required
@require_product_category
def upload():
    current_user = get_current_user()
    if 'upload' not in USER_ROLES[current_user['role']]['permissions']:
        flash('Access denied. Insufficient permissions.', 'error')
        return redirect(url_for('index'))

    product_category = next((cat for cat in PRODUCT_CATEGORIES if cat['id'] == session['product_category']), None)
    return render_template('upload.html',
                         user=current_user,
                         product_category=product_category,
                         user_role=USER_ROLES[current_user['role']])

@app.route('/settings')
@login_required
def settings():
    current_user = get_current_user()
    product_category = None
    if 'product_category' in session:
        product_category = next((cat for cat in PRODUCT_CATEGORIES if cat['id'] == session['product_category']), None)

    return render_template('settings.html',
                         user=current_user,
                         product_category=product_category,
                         user_role=USER_ROLES[current_user['role']])

# API Routes for demo functionality
@app.route('/api/start-session', methods=['POST'])
def start_session():
    data = request.json
    session_id = str(uuid.uuid4())

    # Mock session data
    session_data = {
        "id": session_id,
        "user_id": session.get('user_id', '1'),
        "workflow": data.get('workflow'),
        "product_category": session.get('product_category'),
        "messages": [],
        "created_at": datetime.now().isoformat(),
        "status": "active"
    }

    session['current_session'] = session_data

    return jsonify({
        "session_id": session_id,
        "message": f"Started {data.get('workflow', 'workflow')} session for {session.get('product_category', 'product')}"
    })

@app.route('/api/send-message', methods=['POST'])
def send_message():
    data = request.json
    user_message = data.get('message', '')

    current_session = session.get('current_session', {})
    if not current_session:
        return jsonify({"error": "No active session"}), 400

    # Add user message
    current_session['messages'].append({
        "role": "user",
        "content": user_message,
        "timestamp": datetime.now().isoformat()
    })

    # Mock AI response based on workflow
    workflow = current_session.get('workflow', 'general')
    ai_responses = {
        "contract_qa": [
            "Based on the executed agreement for Supplier X, the termination clause requires 90 days written notice. This is located in Section 12.3 of the document.",
            "The payment terms specify net 30 days from invoice date, with a 2% discount for payments within 10 days.",
            "According to the agreement, the exclusivity period extends for 5 years from the effective date, covering the specified territories."
        ],
        "agreement_replication": [
            "I've analyzed the negotiated terms and identified key differences for New York state requirements. The notice period needs to be extended to 60 days.",
            "California requires specific franchise law disclosures that aren't in the base template. I've added the necessary clauses.",
            "The territory definition for Florida needs to exclude certain counties due to local distribution laws."
        ],
        "financial_analysis": [
            "I've extracted the financial obligations from the agreement. Total annual commitment is $2.4M across quarterly payments.",
            "The marketing fund requirement is 3% of net sales, payable quarterly, with a minimum annual commitment of $50K.",
            "Payment terms analysis shows 70% of obligations are due within 30 days, 25% within 60 days, and 5% within 90 days."
        ]
    }

    default_responses = [
        "I've processed your request and analyzed the relevant documents.",
        "Based on the agreement analysis, here are the key findings:",
        "The system has identified the following relevant information:"
    ]

    responses = ai_responses.get(workflow, default_responses)
    ai_message = random.choice(responses)

    # Add AI message
    current_session['messages'].append({
        "role": "ai",
        "content": ai_message,
        "timestamp": datetime.now().isoformat()
    })

    session['current_session'] = current_session

    return jsonify({
        "ai_message": ai_message,
        "citations": ["Section 4.2", "Page 15", "Clause 8.1"] if workflow == "contract_qa" else []
    })

@app.route('/api/agreement-replication', methods=['POST'])
@login_required
@require_product_category
def agreement_replication_api():
    current_user = get_current_user()
    if 'agreement_replication' not in USER_ROLES[current_user['role']]['permissions']:
        return jsonify({"error": "Access denied. Insufficient permissions."}), 403

    # Check if file was uploaded
    if 'agreement_file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['agreement_file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    # Get selected states and original state
    selected_states = request.form.getlist('states')
    if not selected_states:
        return jsonify({"error": "No states selected"}), 400

    original_state = request.form.get('original_state')
    if not original_state:
        return jsonify({"error": "No original state specified"}), 400

    # Check if original state is in target states
    if original_state in selected_states:
        return jsonify({"error": "Original state cannot be selected as a target state"}), 400

    # Mock processing delay
    import time
    time.sleep(2)

    # Mock replication results
    product_category = next((cat for cat in PRODUCT_CATEGORIES if cat['id'] == session['product_category']), None)

    state_names = {
        "CA": "California",
        "NY": "New York",
        "TX": "Texas",
        "FL": "Florida"
    }

    replication_results = []
    for state in selected_states:
        if state in state_names:
            replication_results.append({
                "state": state,
                "state_name": state_names[state],
                "status": "completed",
                "agreement_id": str(uuid.uuid4()),
                "modifications": [
                    f"Added {state_names[state]} specific termination notice requirements",
                    f"Incorporated {state_names[state]} franchise law disclosures",
                    f"Updated territory definitions for {state_names[state]} compliance"
                ],
                "download_url": f"/api/download-replicated-agreement/{state}"
            })

    return jsonify({
        "success": True,
        "message": f"Successfully replicated agreement for {len(selected_states)} state(s)",
        "results": replication_results,
        "original_filename": file.filename,
        "product_category": product_category['name'] if product_category else "Unknown"
    })

@app.route('/api/download-replicated-agreement/<state>')
@login_required
def download_replicated_agreement(state):
    # Mock agreement content
    mock_agreement = f"""
DISTRIBUTION AGREEMENT - {state} VERSION

This is a mock replicated agreement for {state}.

Key modifications made:
1. Added state-specific termination requirements
2. Incorporated franchise law disclosures
3. Updated territory definitions for compliance

Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""

    from flask import Response
    return Response(
        mock_agreement,
        mimetype='text/plain',
        headers={'Content-Disposition': f'attachment; filename=replicated_agreement_{state}.txt'}
    )

if __name__ == '__main__':
    # Get port from environment variable (Amplify requirement)
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
